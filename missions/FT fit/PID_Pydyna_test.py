#!/usr/bin/env python3
import pydyna
import numpy as np
import matplotlib.pyplot as plt

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
        self.saturated = 0

    def output(self, y):
        error = self.setpoint - y
        diff_error = (error - self.prev_err) / self.dt
        self.int_err += error * self.dt
        output = self.Kp * error + (1-self.saturated) * self.Ki * self.int_err + self.Kd * diff_error
        if output > self.max_output:
            output = self.max_output
            self.saturated = 1
            self.int_err = 0
        else:
            self.saturated = 0
        self.prev_err = error
        return output


class Ship:

    def __init__(self):
        self.sim = pydyna.create_simulation("Navio_L15B4_Conv.p3d")
        self.ship = self.sim.vessels['207']
        self.rudder = self.ship.rudders['0']
        self.propeller = self.ship.thrusters['0']

        self.ship._set_linear_position([0, 0, 0])
        self.ship._set_angular_position([0, 0, 0])
        self.ship._set_linear_velocity([0, 0, 0])

        self.rudder.dem_angle = np.deg2rad(0)
        self.propeller.dem_rotation = 0

        self.speed = list()
        self.rotation = list()
        self.heading = list()
        self.rudder_angle = list()
        self.steps = 4000

        # self.speedPID = myPID(Kp=44.6, Ki=0.822, Kd=0, dt=0.1, max_output=17.5)  # com FT antiga
        # self.speedPID = myPID(Kp=18.53, Ki=0.5379, Kd=0, dt=0.1, max_output=17.5) # sem delay
        self.speedPID = myPID(Kp=4.944, Ki=0.1629, Kd=0, dt=0.1, max_output=17.5)  # com delay
        # self.speedPID = myPID(Kp=6.26, Ki=23.38, Kd=0, dt=0.1, max_output=17.5)  #  Cohen e Coon
        self.coursePID = myPID(Kp=3.97, Ki=0.269, Kd=3.95, dt=0.1, max_output=35)



    def plot_speed(self):
        plt.figure()
        t = np.linspace(0, 0.1*self.steps, self.steps)
        plt.plot(t, self.speed)
        plt.xlabel("t [s]")
        plt.ylabel("velocidade [m/s]")
        #plt.title("Speed x Step")
        plt.show()

    def plot_rotation(self):
        plt.figure()
        t = np.linspace(0, 0.1 * self.steps, self.steps)
        plt.plot(t, self.rotation)
        plt.xlabel("t [s]")
        plt.ylabel("rotação [rps]")
        #plt.title("rotation actuator")
        plt.show()

    def plot_heading(self):
        plt.figure()
        t = np.linspace(0, 0.1 * self.steps, self.steps)
        plt.plot(t, np.rad2deg(self.heading))
        plt.xlabel("t [s]")
        plt.ylabel("aproamento [o]")
        #plt.title("Heading x Step")
        plt.show()

    def plot_rudder(self):
        plt.figure()
        t = np.linspace(0, 0.1 * self.steps, self.steps)
        plt.plot(t, np.rad2deg(self.rudder_angle))
        plt.xlabel("t [s]")
        plt.ylabel("ângulo de leme [o]")
        #plt.title("rudder actuator")
        plt.show()

    def iterate(self):
            self.speedPID.setpoint = 1
            self.coursePID.setpoint = 0
            for i in range(0, self.steps):
                self.propeller.dem_rotation = self.speedPID.output(self.ship.linear_velocity[0])
                self.rudder.dem_angle = -np.deg2rad(self.coursePID.output(np.rad2deg(self.ship.angular_position[2])))
                if i > 2000:
                    self.coursePID.setpoint = 1
                # if i > 4000:
                #     self.coursePID.setpoint = 60
                self.sim.step()
                self.speed.append(self.ship.linear_velocity[0])
                self.rotation.append(self.propeller.dem_rotation)
                self.heading.append(self.ship.angular_position[2])
                self.rudder_angle.append(self.rudder.dem_angle)
            pydyna.destroy_simulation(self.sim)

if __name__ == "__main__":
    ship = Ship()
    ship.iterate()
    ship.plot_rotation()
    ship.plot_speed()
    ship.plot_heading()
    ship.plot_rudder()
