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
        self.prev_y = 0
        self.saturated = 0

    def output(self, y): # diff e
        error = self.setpoint - y
        diff_error = (error - self.prev_err) / self.dt
        self.int_err += error * self.dt
        output = self.Kp * error + (1-self.saturated) * self.Ki * self.int_err + self.Kd * diff_error
        if abs(output) > self.max_output:
            output = output/abs(output)*self.max_output
            self.saturated = 1
            self.int_err = 0
        else:
            self.saturated = 0
        self.prev_err = error
        return output

    # def output(self, y): # diff y
    #     error = self.setpoint - y
    #     diff_error = (y - self.prev_y) / self.dt
    #     self.int_err += error * self.dt
    #     output = self.Kp * error + (1-self.saturated) * self.Ki * self.int_err + self.Kd * diff_error
    #     if abs(output) > self.max_output:
    #         output = output/abs(output)*self.max_output
    #         self.saturated = 1
    #         self.int_err = 0
    #     else:
    #         self.saturated = 0
    #     self.prev_y = y
    #     return output


class PIDcalib:

    def __init__(self, file):

        # simulation
        self.p3d = file
        self.sim = pydyna.create_simulation(self.p3d)
        self.ship = self.sim.vessels['292']
        self.rudder0 = self.ship.rudders['0']
        self.rudder1 = self.ship.rudders['1']
        self.propeller0 = self.ship.thrusters['0']
        self.propeller1 = self.ship.thrusters['1']

        # initial condition
        self.ship._set_linear_position([0, 0, 0])
        self.ship._set_linear_velocity([0, 0, 0])
        self.rudder0.dem_angle = math.radians(0)
        self.rudder1.dem_angle = math.radians(0)
        self.propeller0.dem_rotation = 0
        self.propeller1.dem_rotation = 0
        
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
        self.speedPID = myPID(3.043767878638531, 0.10302242667763199, 0, 0.1, 25.6)
        self.coursePID = myPID(0, 0, 0, 0.1, 30)
        
    def clean(self):
        # simulation
        pydyna.destroy_simulation(self.sim)
        self.sim = pydyna.create_simulation(self.p3d)
        self.ship = self.sim.vessels['292']
        self.rudder0 = self.ship.rudders['0']
        self.rudder1 = self.ship.rudders['1']
        self.propeller0 = self.ship.thrusters['0']
        self.propeller1 = self.ship.thrusters['1']

        # initial condition
        self.ship._set_linear_position([0, 0, 0])
        self.ship._set_linear_velocity([0, 0, 0])
        self.rudder0.dem_angle = math.radians(0)
        self.rudder1.dem_angle = math.radians(0)
        self.propeller0.dem_rotation = 0
        self.propeller1.dem_rotation = 0
        
        # empty lists
        self.rot = list()
        self.course = list()
        self.speed = list()
        self.rotation = list()
        self.rudder_angle = list()

    
    def sim_speed(self):
        self.clean()
        steps = self.steps
        self.propeller0.dem_rotation = self.propeller0.max_rotation/2.2
        self.propeller1.dem_rotation = self.propeller1.max_rotation/2.2
        for i in range(0, steps):
            self.sim.step()
            self.speed.append(self.ship.linear_velocity[0])
        self.speed = np.array(self.speed)

    def fit_speed(self, plot = True, kapa = 1):
        self.sim_speed()

        t  = self.t
        K  = max(self.speed)/self.propeller0.dem_rotation
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
        yout, t = co.step(self.propeller0.dem_rotation*self.speedFT, t)
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
        self.propeller0.dem_rotation = self.propeller0.max_rotation/2.2
        self.propeller1.dem_rotation = self.propeller1.max_rotation/2.2
        for i in range(0, steps):
            self.sim.step()
            self.rot.append(self.ship.angular_velocity[2])
            if i > 1000:
                self.rudder0.dem_angle = math.radians(-10)
                self.rudder1.dem_angle = math.radians(-10)
        self.rot=np.rad2deg(np.array(self.rot[1000:1200]))

    def fit_rot_3(self, plot=True, kapa=1):
        self.clean()
        self.sim_rot()
        res = co.stepinfo(self.rot, T=self.t[1000:1200]-100)
        ts = res['SettlingTime']
        Mp = res['Overshoot']/100
        sigma = 4/ts
        zeta = abs(np.log(Mp))/np.sqrt(np.pi**2 + (np.log(Mp))**2)
        wn = 2*sigma/zeta
        K = -self.rot[-1]/np.rad2deg(self.rudder0.dem_angle)
        #T = 0.2
        self.rotFT = co.tf([K*wn**2],[1, 2*zeta*wn, wn**2]) #*co.tf([1],[T,1])
        print(self.rotFT)
        # self.rotFT_str = str(round(K*wn**2,2))+"/(s²+"+str(round(2*wn*zeta,2))+"s+"+str(round(wn**2,2))+")"
        self.rotFT_str = str(self.rotFT)
        if plot:
            self.plot_rot()

    def fit_rot_2(self, plot=True, kapa=1):
        self.clean()
        self.sim_rot()
        t  = np.linspace(0, 200*self.dt, 200)
        K  = -self.rot[-1]/np.rad2deg(self.rudder0.dem_angle)
        t1  = np.interp(0.283*max(self.rot), self.rot, t)
        t2  = np.interp(0.632*max(self.rot), self.rot, t)
        T = 1.5*(t2-t1)
        theta = t2 - T
        G = co.tf([K], [T, 1])
        num, den = co.pade(theta, n=1)
        delay = co.tf(num, den)
        self.rotFT = G*delay
        self.rotFT_str = "exp(-"+str(round(theta,2))+"s)*"+str(round(K,2))+"/("+str(round(T,2))+"s+1)"
        
        # PID
        self.coursePID.Kp = 1.2*T/K/theta
        self.coursePID.Ki = 1/(2*theta)*self.coursePID.Kp
        self.coursePID.Ki = 0.5*theta*self.coursePID.Kp
        
        print("coursePID = ",[self.coursePID.Kp,self.coursePID.Ki,self.coursePID.Kd])
        if plot:
            self.plot_rot()

    def fit_rot(self, plot=True):
        self.clean()
        self.sim_rot()
        K  = max(self.rot)/np.rad2deg(self.rudder0.dem_angle)
        dt = 0.1
        t  = np.linspace(0, 200*dt, 200)
        T  = np.interp(0.632*max(self.rot), self.rot, t)
        self.rotFT = co.tf([K], [T, 1])
        self.rotFT_str=str(round(K,3))+"/("+str(round(T,3))+"s+1)"
        if plot:
            self.plot_rot()
        
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

    def test_speedPID(self, dem_speed, PID = [], plot = True):
        self.clean()
        self.speedPID.setpoint = dem_speed
        if len(PID)>1:
            self.speedPID.Kp = PID[0]
            self.speedPID.Ki = PID[1]
            self.speedPID.Kd = PID[2]
        for i in range(0, self.steps):
                self.propeller0.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])
                self.propeller1.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])
                self.sim.step()
                self.speed.append(self.ship.linear_velocity[0])
                self.rotation.append(self.propeller0.dem_rotation)
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
        res = co.stepinfo(self.speed, T=self.t)
        label = f"ts2% = {res['SettlingTime']:2.2f} s \n"
        label += f"Mp = {res['Overshoot']:2.2f} %\n"
        label += f"y_final = {res['SteadyStateValue']:2.2f} m/s"
        plt.annotate(label, xy =(10, 1),xytext =(40, max(self.speed)/2),bbox=dict(boxstyle="round", fc="w"))

        plt.show()

    def test_coursePID(self, dem_course, dem_speed = 4, PID = [], plot = True, analisys = True):
        self.clean()
        self.steps = 4000
        self.t  = np.linspace(0, self.steps*self.dt, self.steps)

        self.ship._set_linear_velocity([dem_speed, 0, 0])
        self.speedPID.setpoint = dem_speed
        self.propeller0.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])
        self.propeller1.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])        
        
        self.coursePID.setpoint = 0
        if len(PID)>1:
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
                self.rudder0.dem_angle = -np.deg2rad(self.coursePID.output(np.rad2deg(self.ship.angular_position[2])))
                self.rudder1.dem_angle = -np.deg2rad(self.coursePID.output(np.rad2deg(self.ship.angular_position[2])))
                self.propeller0.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])
                self.propeller1.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])
                self.sim.step()
                self.speed.append(self.ship.linear_velocity[0])
                self.rotation.append(self.propeller0.dem_rotation)
                self.course.append(self.ship.angular_position[2])
                self.rudder_angle.append(self.rudder0.dem_angle)
        if plot:
            self.plot_coursePID(analisys)

    def plot_coursePID(self, analisys = True):
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
        if analisys:
            res = co.stepinfo(self.speed[1000:2000], T=self.t[1000:2000])
            label = f"ts2% = {res['SettlingTime']-100:2.2f} s \n"
            label += f"Mp = {res['Overshoot']:2.2f} %\n"
            label += f"y_final = {res['SteadyStateValue']:2.2f} m/s"
            plt.annotate(label, xy =(10, 1),xytext =(120, 2.5),bbox=dict(boxstyle="round", fc="w"))
            res = co.stepinfo(self.speed[2000:3000], T=self.t[2000:3000])
            label = f"ts2% = {res['SettlingTime']-200:2.2f} s \n"
            label += f"Mp = {res['Overshoot']:2.2f} %\n"
            label += f"y_final = {res['SteadyStateValue']:2.2f} m/s"
            plt.annotate(label, xy =(10, 1),xytext =(220, 2.5),bbox=dict(boxstyle="round", fc="w"))
            res = co.stepinfo(self.speed[3000:4000], T=self.t[3000:4000])
            label = f"ts2% = {res['SettlingTime']-300:2.2f} s \n"
            label += f"Mp = {res['Overshoot']:2.2f} %\n"
            label += f"y_final = {res['SteadyStateValue']:2.2f} m/s"
            plt.annotate(label, xy =(10, 1),xytext =(320, 2.5),bbox=dict(boxstyle="round", fc="w"))

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
        if analisys:
            res = co.stepinfo(self.course[1000:2000], T=self.t[1000:2000])
            label = f"ts2% = {res['SettlingTime']-100:2.2f} s \n"
            label += f"Mp = {res['Overshoot']:2.2f} %\n"
            label += f"y_final = {np.rad2deg(res['SteadyStateValue']):2.2f} o"
            plt.annotate(label, xy =(10, 1),xytext =(120, 5),bbox=dict(boxstyle="round", fc="w"))
            res = co.stepinfo(self.course[2000:3000], T=self.t[2000:3000])
            label = f"ts2% = {res['SettlingTime']-200:2.2f} s \n"
            label += f"Mp = {res['Overshoot']:2.2f} %\n"
            label += f"y_final = {np.rad2deg(res['SteadyStateValue']):2.2f} o"
            plt.annotate(label, xy =(10, 1),xytext =(220, 10),bbox=dict(boxstyle="round", fc="w"))
            res = co.stepinfo(self.course[3000:4000], T=self.t[3000:4000])
            label = f"ts2% = {res['SettlingTime']-300:2.2f} s \n"
            label += f"Mp = {res['Overshoot']:2.2f} %\n"
            label += f"y_final = {np.rad2deg(res['SteadyStateValue']):2.2f} o"
            plt.annotate(label, xy =(10, 1),xytext =(320, 15),bbox=dict(boxstyle="round", fc="w"))

        plt.show()

    def ZN_PID(self, Kpu, Pu):
        Kp = 0.6*Kpu
        Ti = Pu/2
        Td = Pu/8
        print("coursePID = ",[Kp,Kp/Ti,Kp*Td])
        return [Kp, Kp/Ti, Kp*Td]

    def ZN_PID_no(self, Kpu, Pu):
        Kp = 0.2*Kpu
        Ti = Pu/2
        Td = Pu/3
        return [Kp, Kp/Ti, Kp*Td]



if __name__ == "__main__":
    p3d = "NACMM_2021.p3d"
    calib = PIDcalib(p3d)
    # calib.fit_speed(plot = True, kapa = 1)
    # calib.test_speedPID(dem_speed = 4)
    calib.fit_rot_3()
    # calib.test_coursePID(dem_course = [10, 10, 10], dem_speed = 4, PID = [6,0,0], analisys = False)
    # PID = calib.ZN_PID(Kpu = 6, Pu = 254-246) # PID e
    # calib.test_coursePID(dem_course = [15,45,30], dem_speed = 4, PID = PID)



