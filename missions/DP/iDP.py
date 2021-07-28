#!/usr/bin/env python3
import pymoos
import time
import sys
import numpy as np
import pydyna
import inhousedp
from MoosReader import MoosReader

class iDP(pymoos.comms):

    def __init__(self, moos_community, moos_port):
        """Initiates MOOSComms, sets the callbacks and runs the loop"""
        super(iDP, self).__init__()
        self.server = moos_community
        self.port = moos_port
        self.name = 'iDP'

        self.set_on_connect_callback(self.__on_connect)
        self.set_on_mail_callback(self.__on_new_mail)

        self.add_active_queue('desired_queue', self.on_desired_message)
        self.add_message_route_to_active_queue('desired_queue', 'DESIRED_SURGE')
        self.add_message_route_to_active_queue('desired_queue', 'DESIRED_SWAY')
        self.add_message_route_to_active_queue('desired_queue', 'DESIRED_YAW')

        # self.add_active_queue('nav_queue', self.on_nav_message)
        # self.add_message_route_to_active_queue('nav_queue', 'NAV_X')
        # self.add_message_route_to_active_queue('nav_queue', 'NAV_Y')
        # self.add_message_route_to_active_queue('nav_queue', 'NAV_HEADING')
        
        file = sys.argv[1]
        params=MoosReader(file,"iDP")

        self.desired_surge=0
        self.desired_sway=0
        self.desired_yaw=0
        self.real_x=0
        self.real_y=0
        self.real_speed=0
        self.real_heading=0
        self.dt=0.1
        
        p3d = "Maersk Handler.p3d"
        self.my_dyna = pydyna.create_simulation(p3d)
        self.my_vessel = self.my_dyna.vessels['42']
        self.my_vessel.linear_position = [self.real_x, self.real_y, -6.6]
        self.my_vessel.angular_position = [0.0, 0.0, (90-self.real_heading)*np.pi/180]
        self.my_dp = inhousedp.InhouseDP("/home/lhscaldas/moos-ivp-lhscaldas/missions/DP/"+p3d, 42)

        self.run(self.server, self.port, self.name)
        pymoos.set_moos_timewarp(params['MOOSTimeWarp'])


    def __on_connect(self):
        """OnConnect callback"""
        print("Connected to", self.server, self.port,
              "under the name ", self.name)
        self.notify('NAV_DEPTH', float(0), -1)
        return (self.register('DESIRED_SURGE', 0) and
                self.register('DESIRED_SWAY', 0) and
                self.register('DESIRED_YAW', 0))

    def __on_new_mail(self):
        """OnNewMail callback"""
        for msg in self.fetch():
            pass
        return True

    def on_desired_message(self, msg):
        """Special callback for Desired"""
        if msg.key() == 'DESIRED_SURGE':
            self.desired_surge = msg.double()
        elif msg.key() == 'DESIRED_SWAY':
            self.desired_sway = msg.double()
        elif msg.key() == 'DESIRED_YAW':
            self.desired_yaw = msg.double()
        return True

    # def on_nav_message(self, msg):
    #     """Special callback for Sensor"""
    #     if msg.key() == 'NAV_SPEED':
    #         self.sensor_speed = msg.double() # m/s
    #     elif msg.key() == 'NAV_HEADING':
    #         self.sensor_heading = msg.double() # graus
    #     return True

    # def on_ivphelm_message(self, msg):
    #     """Special callback for Ivphelm"""
    #     if msg.key() == 'IVPHELM_ALLSTOP':
    #         self.manual = msg.string()
    #     return True


    def send(self, key, value):
        self.notify(key, value, -1)

    def update(self):
        self.send('NAV_SPEED', self.real_speed)
        self.send('NAV_HEADING', self.real_heading)
        self.send('NAV_X', self.real_x)
        self.send('NAV_Y', self.real_y)

    def debug(self, my_thrusters):
        print(" ")
        print(" ")
        print(" ")
        print("iDP Debug")
        for one_thr in my_thrusters:
            print(self.my_vessel.thrusters[one_thr].dem_rotation)
            print(self.my_vessel.thrusters[one_thr].dem_pitch*180/np.pi)
            print(self.my_vessel.thrusters[one_thr].dem_angle*180/np.pi)

    def calculate_heading(self):
        real_heading = 0
        i = 0
        j = 0
        real_yaw = self.my_vessel.angular_position[2]
        real_heading = 90 - np.rad2deg(real_yaw)
        if real_heading < 0:
            i = abs(real_heading) // 360 + 1
            real_heading += 360*i
        if real_heading > 360:
            j = abs(real_heading) // 360
            real_heading -= 360*j
        return real_heading


    def iterate(self):
        dt = self.dt
        dt_fast_time = dt/pymoos.get_moos_timewarp()
        while True:
            time.sleep(dt_fast_time)
           
            # Atualiza setpoint
            self.my_dp.setreference([self.desired_surge, self.desired_sway, (90-self.desired_yaw)*np.pi/180])

            # Iteração do inHouseDP
            my_var = self.my_dp.dostep([self.my_vessel.linear_position[0],
                                    self.my_vessel.linear_position[1],
                                    self.my_vessel.angular_position[2]])

            # Atualiza atuadores
            my_thrusters = list(self.my_vessel.thrusters)
            for one_thr in my_thrusters:
                self.my_vessel.thrusters[one_thr].dem_rotation = my_var[one_thr].getDemandedRps()
                self.my_vessel.thrusters[one_thr].dem_pitch = my_var[one_thr].getDemandedPod()
                self.my_vessel.thrusters[one_thr].dem_angle = my_var[one_thr].getDemandedAzimuth()

            # Atualiza estado
            self.real_x=self.my_vessel.linear_position[0]
            self.real_y=self.my_vessel.linear_position[1]
            self.real_speed=self.my_vessel.linear_velocity[0]
            self.real_heading = self.calculate_heading()
            
            # Iteração do Pydyna
            self.my_dyna.step()
            self.update()
            self.debug(my_thrusters)


def main():
    DPcontrol = iDP('localhost', 9000)
    DPcontrol.iterate()


if __name__ == "__main__":
    main()
