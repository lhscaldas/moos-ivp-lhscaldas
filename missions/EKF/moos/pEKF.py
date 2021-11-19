#!/usr/bin/env python3
import pymoos
import time
import sys
import numpy as np
from MoosReader import MoosReader

sin = np.sin
cos = np.cos
rho=1025e-3
# diâmetros dos propulsores
D1=0.475
D2=0.475
D3=0.185
# posição dos propulsores
x1=5.52
y1=0.67
x2=5.52
y2=0.67
x3=5.78
# medidas do navio
h = 1.65 # altura
B = 3.379 # boca
T = 0.956 # calado
L = 13.095 # LOA
# massas e amortecimento
C2_90  = 3.27607
C1_180 = 0.10900
m11=18.79+1.01115
m22=18.79+10.48726
m33=240.19+90.95633
d11=rho*B*T*C1_180/2
d22=rho*L*T*C2_90/2
d33=rho*L**4*T*C2_90/32

def F(eta,tau,dt):
    


class pEKF(pymoos.comms):

    def __init__(self, params):
        """Initiates MOOSComms, sets the callbacks and runs the loop"""
        super(pEKF, self).__init__()
        self.server = 'localhost'
        self.port = int(params['ServerPort'])
        self.name = 'pEKF'

        self.set_on_connect_callback(self.__on_connect)
        self.set_on_mail_callback(self.__on_new_mail)

        self.add_active_queue('dvl_queue', self.on_dvl_message)
        self.add_message_route_to_active_queue('dvl_queue', 'DVL_SPEED')

        self.add_active_queue('gps_queue', self.on_gps_message)
        self.add_message_route_to_active_queue('gps_queue', 'GPS_SPEED')
        self.add_message_route_to_active_queue('gps_queue', 'GPS_X')
        self.add_message_route_to_active_queue('gps_queue', 'GPS_Y')

        self.add_active_queue('gyro_queue', self.on_gyro_message)
        self.add_message_route_to_active_queue('gyro_queue', 'GYRO_HEADING')
        
        self.add_active_queue('imu_queue', self.on_imu_message)
        self.add_message_route_to_active_queue('imu_queue', 'IMU_SPEED')
        self.add_message_route_to_active_queue('imu_queue', 'IMU_X')
        self.add_message_route_to_active_queue('imu_queue', 'IMU_Y')
        self.add_message_route_to_active_queue('imu_queue', 'IMU_HEADING')

        self.add_active_queue('desired_queue', self.on_desired_message)
        self.add_message_route_to_active_queue('desired_queue', 'DESIRED_ROTATION')
        self.add_message_route_to_active_queue('desired_queue', 'DESIRED_RUDDER')

        self.dvl_speed = 0
        self.gps_speed = 0
        self.gps_x = 0
        self.gps_y = 0
        self.gyro_heading = 0
        self.imu_speed = 0
        self.imu_x = 0
        self.imu_y = 0
        self.imu_heading = 0
        
        self.ekf_speed = 0
        self.ekf_x = params['START_X']
        self.ekf_y = params['START_Y']
        self.ekf_heading = params['START_HEADING']

        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.beta1 = 0
        self.beta2 = 0
        

        
        
        self.run(self.server, self.port, self.name)
        pymoos.set_moos_timewarp(params['MOOSTimeWarp'])
        self.dt=0.1

       

    def __on_connect(self):
        """OnConnect callback"""
        print("Connected to", self.server, self.port,
              "under the name ", self.name)
        return (self.register('DVL_SPEED', 0) and
                self.register('GPS_SPEED', 0) and
                self.register('GPS_X', 0) and
                self.register('GPS_Y', 0) and
                self.register('GYRO_HEADING', 0) and
                self.register('IMU_SPEED', 0) and
                self.register('IMU_X', 0) and
                self.register('IMU_Y', 0) and
                self.register('IMU_HEADING', 0) and
                self.register('DESIRED_ROTATION', 0) and
                self.register('DESIRED_RUDDER', 0))
                

    def __on_new_mail(self):
        """OnNewMail callback"""
        for msg in self.fetch():
            pass
        return True

    def on_dvl_message(self, msg):
        """Special callback for Desired"""
        if msg.key() == 'DVL_SPEED':
            self.dvl_speed = msg.double()
        return True

    def on_gps_message(self, msg):
        """Special callback for Desired"""
        if msg.key() == 'GPS_SPEED':
            self.gps_speed = msg.double()
        elif msg.key() == 'GPS_X':
            self.gps_x = msg.double()
        elif msg.key() == 'GPS_Y':
            self.gps_y = msg.double()
        return True

    def on_gyro_message(self, msg):
        """Special callback for Desired"""
        if msg.key() == 'GYRO_HEADING':
            self.gyro_heading = msg.double()
        return True

    def on_imu_message(self, msg):
        """Special callback for Desired"""
        if msg.key() == 'IMU_SPEED':
            self.imu_speed = msg.double()
        elif msg.key() == 'IMU_X':
            self.imu_x = msg.double()
        elif msg.key() == 'IMU_Y':
            self.imu_y = msg.double()
        elif msg.key() == 'IMU_HEADING':
            self.imu_heading = msg.double()
        return True

    def on_desired_message(self, msg):
        """Special callback for Desired"""
        if msg.key() == 'DESIRED_RUDDER':
            self.beta1 = msg.double()
            self.beta2 = msg.double()
        elif msg.key() == 'DESIRED_ROTATION':
            self.n1 = msg.double()
            self.n2 = msg.double()
        return True



    def send(self, key, value):
        self.notify(key, value, -1)

    def update(self):
        pass
        # self.send('DESIRED_RUDDER', self.desired_rudder)
        # self.send('DESIRED_ROTATION', self.desired_rotation)

    def estimate_inputs(self):
        # calculo do thrust
        u = self.ekf_speed
        n1 = self.n1
        n2 = self.n2
        n3 = self.n3
        if n1 != 0:
            J1=u/(n1*D1)
        else:
            J1=0
        if n2 != 0:
            J2=u/(n2*D2)
        else:
            J2=0
        if n3 != 0:
            J3=u/(n3*D3)
        else:
            J3=0
        Kt1=1.09214295e-01*J1**5 - 1.89739146e-05*J1**4 - 1.91249589e-01*J1**3 + 6.59504311e-06*J1**2 - 4.14551312e-01*J1 + 6.58016406e-01
        Kt2=1.09214295e-01*J2**5 - 1.89739146e-05*J2**4 - 1.91249589e-01*J2**3 + 6.59504311e-06*J2**2 - 4.14551312e-01*J2 + 6.58016406e-01
        Kt3=0.01476418*J3**5 - 0.03187213*J3**4 - 0.38456785*J3**3 + 0.19234734*J3**2 - 0.49985203*J3 + 0.36826644
        T1=rho*Kt1*n1**2*D1**4
        T2=rho*Kt2*n2**2*D2**4
        T3=rho*Kt3*n3**2*D3**4
        # calculo da deflexão
        beta1 = self.beta1 # leme 1
        beta2 = self.beta2 # leme 2
        alfa1 = np.deg2rad(-2.18096324e-04*beta1**3 + 1.05990036*beta1) # deflexão 1
        alfa2 = np.deg2rad(-2.18096324e-04*beta2**3 + 1.05990036*beta2) # deflexão 2
        # calculo das entradas
        Tao_u = T1*cos(alfa1)+T2*cos(alfa2)
        Tao_v = T1*sin(alfa1)+T2*sin(alfa2)+T3
        Tao_r = -T1*cos(alfa1)*y1-T1*sin(alfa1)*x1+T2*cos(alfa2)*y2-T2*sin(alfa2)*x2-T3*x3
        # return [Tao_u,Tao_v,Tao_r,T1,T2,T3,alfa1,alfa2]
        return [Tao_u,Tao_v,Tao_r]


    def debug(self):
        print(" ")
        print(" ")
        print(" ")
        print("pEKF Debug")
        # print(f"EKF_SPEED = {self.ekf_speed}")
        # print(f"EKF_X = {self.ekf_x}")
        # print(f"EKF_Y = {self.ekf_y}")
        # print(f"EKF_HEADING = {self.ekf_heading}")
        tau = self.estimate_inputs()
        


    def iterate(self):
        dt = self.dt*10
        dt_fast_time = dt/pymoos.get_moos_timewarp()
        while True:
            time.sleep(dt_fast_time)
            # self.ekf_speed = (self.gps_speed+self.dvl_speed+self.imu_speed)/3
            # self.ekf_x = (self.gps_x+self.imu_x)/2
            # self.ekf_y = (self.gps_y+self.imu_y)/2
            # self.ekf_heading = (self.gyro_heading+self.imu_heading)/2

            

            # self.update()
            self.debug()


if __name__ == "__main__":
    file = sys.argv[1] 
    params=MoosReader(file,"pEKF")
    PIDcontrol = pEKF(params)
    PIDcontrol.iterate()
