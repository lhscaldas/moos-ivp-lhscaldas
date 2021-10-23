import pydyna
import math
import matplotlib.pyplot as plt
import numpy as np
import control.matlab as co

class myPID:

    def __init__(self, Kp, Ki, Kd, dt, max_output):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        self.max_output = max_output

        self.setpoint = 0
        self.int_err = 0
        self.prev_err = 0
        # self.prev_y = 0
        self.saturated = 0

    def output(self, y):
        error = self.setpoint - y
        diff_error = (error - self.prev_err) / self.dt
        # diff_error = (y - self.prev_y) / self.dt
        self.int_err += error * self.dt
        output = self.Kp * error + (1-self.saturated) * self.Ki * self.int_err + self.Kd * diff_error
        if abs(output) > self.max_output:
            output = output/abs(output)*self.max_output
            self.saturated = 1
            self.int_err = 0
        else:
            self.saturated = 0
        self.prev_err = error
        # self.prev_y = y
        return output


class PIDcalib:

    def __init__(self, file):

        # simulation
        self.p3d = file
        self.sim = pydyna.create_simulation(self.p3d)
        self.ship = self.sim.vessels['207']
        self.rudder = self.ship.rudders['0']
        self.propeller = self.ship.thrusters['0']

        # initial condition
        self.ship._set_linear_position([0, 0, 0])
        self.ship._set_linear_velocity([0, 0, 0])
        self.rudder.dem_angle = math.radians(0)
        self.propeller.dem_rotation = 0
        
        # empty lists
        self.rot = list()
        self.course = list()
        self.speed = list()
        self.rotation = list()
        self.rudder_angle = list()

        # FT aproximation
        self.speedFT = co.tf(1,1)
        self.speedFT_str = " "
        self.rotFT = co.tf(1,1)
        self.rotFT_str = " "

        # Time data
        self.steps = 2000
        self.dt = 0.1
        self.t  = np.linspace(0, self.steps*self.dt, self.steps)

        # PID
        self.speedPID = myPID(31.326655882217, 0.849957626760817, 0, 0.1, 17.5)
        self.coursePID = myPID(0, 0, 0, 0.1, 35)
        
    def clean(self):
        # simulation
        pydyna.destroy_simulation(self.sim)
        self.sim = pydyna.create_simulation(self.p3d)
        self.ship = self.sim.vessels['207']
        self.rudder = self.ship.rudders['0']
        self.propeller = self.ship.thrusters['0']

        # initial condition
        self.ship._set_linear_position([0, 0, 0])
        self.ship._set_linear_velocity([0, 0, 0])
        self.rudder.dem_angle = math.radians(0)
        self.propeller.dem_rotation = 0
        
        # empty lists
        self.rot = list()
        self.course = list()
        self.speed = list()
        self.rotation = list()
        self.rudder_angle = list()

    
    def sim_speed(self):
        self.clean()
        steps = self.steps
        self.propeller.dem_rotation = self.propeller.max_rotation/5.4
        for i in range(0, steps):
            self.sim.step()
            self.speed.append(self.ship.linear_velocity[0])
        self.speed = np.array(self.speed)

    def fit_speed(self, plot = True, kapa = 1):
        self.sim_speed()

        t  = self.t
        K  = max(self.speed)/self.propeller.dem_rotation
        t1  = np.interp(0.283*max(self.speed), self.speed, t)
        t2  = np.interp(0.632*max(self.speed), self.speed, t)
        T = 1.5*(t2-t1)
        theta = t2 - T
        G = co.tf([K], [T, 1])
        num, den = co.pade(theta, n=1)
        delay = co.tf(num, den)
        self.speedFT = G*delay
        self.speedFT_str = "exp(-"+str(round(theta,2))+"s)*"+str(round(K,2))+"/("+str(round(T,2))+"s+1)"

        # PI
        self.speedPID.Kp = 0.9*T/K/theta * kapa
        self.speedPID.Ki = 0.3/theta*self.speedPID.Kp
        
        # PID
        # self.speedPID.Kp = 1.2*T/K/theta
        # self.speedPID.Ki = 1/(2*theta)*self.speedPID.Kp
        # self.speedPID.Ki = 0.5*theta*self.speedPID.Kp
        
        print("speedPID = ",[self.speedPID.Kp,self.speedPID.Ki,self.speedPID.Kd])
        if plot:
            self.plot_speed()

    
    def plot_speed(self):
        t = self.t
        yout, t = co.step(self.propeller.dem_rotation*self.speedFT, t)
        plt.figure()
        plt.plot(t, self.speed, label="Pydyna")
        plt.plot(t, yout, label=self.speedFT_str)
        plt.xlabel("tempo [s]")
        plt.ylabel("velocidade [m/s]")
        plt.title("Resposta da Velocidade Linear")
        plt.legend()
        plt.show()


    def sim_rot(self):
        self.clean()
        steps = self.steps
        self.propeller.dem_rotation = self.propeller.max_rotation/5.4
        for i in range(0, steps):
            self.sim.step()
            self.rot.append(self.ship.angular_velocity[2])
            if i > 1000:
                self.rudder.dem_angle = math.radians(-10)
        self.rot=np.rad2deg(np.array(self.rot[1000:1200]))

    def fit_rot(self):
        K  = -max(self.rot)/np.rad2deg(self.rudder.dem_angle)
        dt = 0.1
        t  = np.linspace(0, 200*dt, 200)
        T  = np.interp(0.632*max(self.rot), self.rot, t)
        self.rotFT = co.tf([K], [T, 1])
        self.rotFT_str=str(round(K,3))+"/("+str(round(T,3))+"s+1)"
        
    def plot_rot(self):
        dt = self.dt
        t  = np.linspace(0, 200*dt, 200)
        yout, t = co.step(10*self.rotFT, t)
        plt.figure()
        plt.plot(t, self.rot, label="Pydyna")
        plt.plot(t, yout, label=self.rotFT_str)
        plt.xlabel("tempo [s]")
        plt.ylabel("velocidade angular [o/s]")
        plt.title("Resposta do Velocidade Angular")
        plt.legend()
        plt.show()

    def fit(self):
        # Speed fit
        self.sim_speed()
        self.fit_speed()
        self.plot_speed()
        
        # ROT fit
        self.sim_rot()
        self.fit_rot()
        self.plot_rot()

    def test_speedPID(self, dem_speed, PID = [], plot = True):
        self.clean()
        self.speedPID.setpoint = dem_speed
        if len(PID)>1:
            self.speedPID.Kp = PID[0]
            self.speedPID.Ki = PID[1]
            self.speedPID.Kd = PID[2]
        for i in range(0, self.steps):
                self.propeller.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])
                self.sim.step()
                self.speed.append(self.ship.linear_velocity[0])
                self.rotation.append(self.propeller.dem_rotation)
        if plot:
            self.plot_speedPID()

    def plot_speedPID(self):
        plt.figure
        plt.subplot(121)
        plt.plot(self.t, self.rotation)
        plt.xlabel("t [s]")
        plt.ylabel("rotação [rps]")
        plt.title("Esforço de Controle (rotação)")

        plt.subplot(122)
        plt.plot(self.t, self.speed)
        plt.xlabel("t [s]")
        plt.ylabel("velocidade [m/s]")
        plt.title("Resposta do PID de velocidade")

        plt.show()

    def test_coursePID(self, dem_course, dem_speed = 4, PID = [], plot = True):
        self.clean()
        self.steps = 4000
        self.t  = np.linspace(0, self.steps*self.dt, self.steps)

        self.ship._set_linear_velocity([dem_speed, 0, 0])
        self.speedPID.setpoint = dem_speed
        self.propeller.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])    
        
        self.coursePID.setpoint = 0
        self.coursePID.Kp = PID[0]
        self.coursePID.Ki = PID[1]
        self.coursePID.Kd = PID[2]
        for i in range(0, self.steps):
                if i>1000:
                    self.coursePID.setpoint = dem_course[0]
                if i>2000:
                    self.coursePID.setpoint = dem_course[1]
                if i>3000:
                    self.coursePID.setpoint = dem_course[2]
                self.rudder.dem_angle = -np.deg2rad(self.coursePID.output(np.rad2deg(self.ship.angular_position[2])))
                self.propeller.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])
                self.sim.step()
                self.speed.append(self.ship.linear_velocity[0])
                self.rotation.append(self.propeller.dem_rotation)
                self.course.append(self.ship.angular_position[2])
                self.rudder_angle.append(self.rudder.dem_angle)
        if plot:
            self.plot_coursePID()

    def plot_coursePID(self):
        plt.figure
        plt.subplot(221)
        plt.plot(self.t, self.rotation)
        plt.xlabel("t [s]")
        plt.ylabel("rotação [rps]")
        plt.title("Esforço de Controle (rotação)")

        plt.subplot(222)
        plt.plot(self.t, self.speed)
        plt.xlabel("t [s]")
        plt.ylabel("velocidade [m/s]")
        plt.title("Resposta do PID de velocidade")
        plt.axis([0,400,0,7])

        plt.subplot(223)
        plt.plot(self.t, np.rad2deg(self.rudder_angle))
        plt.xlabel("t [s]")
        plt.ylabel("ângulo de leme [o]")
        plt.title("Esforço de Controle (leme)")

        plt.subplot(224)
        plt.plot(self.t, np.rad2deg(self.course))
        plt.xlabel("t [s]")
        plt.ylabel("aproamento [o]")
        plt.title("Resposta do PID de rumo")

        plt.show()

    def ZN_PID(self, Kpu, Pu):
        Kp = 0.6*Kpu
        Ti = Pu/2
        Td = Pu/8
        return [Kp, Kp/Ti, Kp*Td]

    def ZN_PID_no(self, Kpu, Pu):
        Kp = 0.2*Kpu
        Ti = Pu/2
        Td = Pu/3
        return [Kp, Kp/Ti, Kp*Td]



if __name__ == "__main__":
    p3d = "Navio_L15B4_Conv.p3d"
    calib = PIDcalib(p3d)
    calib.fit_speed(plot = False, kapa = 6)
    # calib.test_speedPID(dem_speed = 4)
    # calib.test_coursePID(dem_course = 10, dem_speed = 4, PID = [15,0,0])
    PID = calib.ZN_PID(Kpu = 15, Pu = 49-35)
    calib.test_coursePID(dem_course = [15,45,30], dem_speed = 4, PID = PID)



