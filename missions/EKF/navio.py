import pydyna
import math
import matplotlib.pyplot as plt
import numpy as np
import control.matlab as co

class Navio:

    def __init__(self, s):   
        # Simulation
        self.steps = 2000
        self.dt = 0.1
        self.t  = np.linspace(0, self.steps*self.dt, self.steps)
        # Pydyna
        self.sim = pydyna.create_simulation("NCMMA_2021.p3d")
        self.ship = self.sim.vessels['292']
        self.rudder0 = self.ship.rudders['0']
        self.rudder1 = self.ship.rudders['1']
        self.propeller0 = self.ship.thrusters['0']
        self.propeller1 = self.ship.thrusters['1']
        self.ship._set_linear_position([0, 0, 0])
        self.ship._set_linear_velocity([0, 0, 0])
        self.rudder0.dem_angle = math.radians(0)
        self.rudder1.dem_angle = math.radians(0)
        # Real Model
        self.m11=19.8011
        self.d11=0.8208
        self.b11=0.1012
        # Control
        self.dm=0.1
        self.gm=0.1
        self.gamma=1e-7
        d0=0.0015
        b0=0.01
        g0=0.0049
        self.a_s=[self.gm/g0]
        self.a_u=[(d0-self.dm)/g0]
        self.a_uu = [b0/g0]
        self.n = [0]
        # self.s, T = co.step(s*(co.tf([1],[2,1]))**3, T=self.t)
        # self.s = s*np.sin(0.03*self.t)
        self.s = s*np.ones((self.steps,))
        self.um = [0]
        self.z = [0]
        # States
        self.u = [0]
        # Sensores
        self.bias=[0.03,0.002,(5e-3)*9.81*self.dt]
        self.u_gps=[0]
        self.u_dvl=[0]
        self.u_imu=[0]
        # EKF
        self.d=d0
        self.b=b0
        self.g=g0
        self.R=np.diag([c**2 for c in self.bias])
        self.Q=1
        self.P=10
        self.u_ekf=[0]

    def control(self, i, u):
        # control effort
        n=self.a_s[i]*self.s[i]+self.a_u[i]*u+self.a_uu[i]*u*abs(u)
        self.n.append(np.sign(n)*np.sqrt(abs(n)))
        # model update
        self.um.append(self.um[i]+(-self.dm*self.um[i]+self.gm*self.s[i])*self.dt)
        # error update
        self.z.append(self.um[i]-u)
        # parameters update
        self.a_s.append(self.a_s[i]-self.gamma*self.z[i]*self.s[i]*self.dt)
        self.a_u.append(self.a_u[i]-self.gamma*self.z[i]*u*self.dt)
        self.a_uu.append(self.a_uu[i]-self.gamma*self.z[i]*u*abs(u)*self.dt)

    def run(self):
        for i in range(0, self.steps-1):
            self.control(i, self.u_ekf[i])
            self.propeller0.dem_rotation=self.n[i+1]
            self.propeller1.dem_rotation=self.n[i+1]
            self.sim.step()
            self.u.append(self.ship.linear_velocity[0])
            self.sensores(i)
            self.EKF(i)
        pydyna.destroy_simulation(self.sim)
        
    def analyse(self):
        print(co.stepinfo(self.u, T=self.t))
        
    def params(self):
        D=0.8
        J=np.array(self.u)/(np.array(self.n)+1e-12)/D
        Kt=0.32-0.1648*J-0.2163*J**2+0.0648*J**3-0.0037*J**4
        eta=0.8
        rho=1025e-3
        
        plt.figure()
        # Calc g
        plt.subplot(511)
        g=2*eta*Kt*rho*D**4/self.m11
        ghat=np.array(self.gm)/np.array(self.a_s)
        plt.plot(self.t, ghat,  label="estimated")
        plt.plot(self.t, g, "k--", label="real")
        plt.xlabel("time [s]")
        plt.ylabel("g")
        plt.title("Parameter g estimation")
        plt.legend()
        # Calc d
        plt.subplot(513)
        d=self.d11/self.m11*np.ones((self.steps,))
        dhat=np.array(self.a_u)*g+self.dm
        plt.plot(self.t, dhat,  label="estimated")
        plt.plot(self.t, d, "k--", label="real")
        plt.xlabel("time [s]")
        plt.ylabel("d")
        plt.title("Parameter d estimation")
        plt.legend()
        # Calc b
        plt.subplot(515)
        b=self.b11/self.m11*np.ones((self.steps,))
        bhat=np.array(self.a_uu)*g
        plt.plot(self.t, bhat,  label="estimated")
        plt.plot(self.t, b, "k--", label="real")
        plt.xlabel("time [s]")
        plt.ylabel("b")
        plt.title("Parameter b estimation")
        plt.legend()
        plt.show()


    def plot_u(self):
        res = co.stepinfo(self.u, T=self.t)
        fig, ax = plt.subplots()
        ax.annotate(f"Settling Time = {res['SettlingTime']:2.2f} s", xy =(10, 1),xytext =(100, max(self.s)/2),bbox=dict(boxstyle="round", fc="w"))
        ax.plot(self.t, self.u, label="real")
        ax.plot(self.t, self.u_ekf, label="ekf")
        ax.plot(self.t, self.um, "k--", label="model")
        plt.xlabel("time [s]")
        plt.ylabel("speed [m/s]")
        plt.title("Speed Response")
        plt.legend()
        plt.show()

    def plot_z(self):
        plt.figure()
        plt.plot(self.t, self.z)
        plt.xlabel("time [s]")
        plt.ylabel("speed error [m/s]")
        plt.title("Error")
        plt.show()
        
    def plot_n(self):
        plt.figure()
        plt.plot(self.t, self.n)
        plt.xlabel("time [s]")
        plt.ylabel("rotation [rps]")
        plt.title("Control Effort")
        plt.show()
        
    def sensores(self, i):
        k=1
        self.u_gps.append(self.u[i]+self.u[i]*k*self.bias[0]*np.random.rand())
        self.u_dvl.append(self.u[i]-self.u[i]*k*self.bias[1]*np.random.rand())
        self.u_imu.append(self.u[i]-self.u[i]*k*self.bias[2]*np.random.rand())
        
    def plot_sensores(self):
        plt.figure()
        plt.plot(self.t, self.u_gps, label="GPS")
        plt.plot(self.t, self.u_dvl, label="DVL")
        plt.plot(self.t, self.u_imu, label="IMU")
        plt.plot(self.t, self.u_ekf, label="EKF")
        plt.plot(self.t, self.u, "k--", label="Real")
        plt.xlabel("time [s]")
        plt.ylabel("speed [m/s]")
        plt.title("Sensors")
        plt.legend()
        plt.show()
        
    def EKF(self,i):
        dt=self.dt
        P=np.array(self.P)
        mi=self.u_ekf[i]
        z=np.array([self.u_gps[i],self.u_dvl[i],self.u_imu[i]])
        d0=self.d
        b0=self.b
        g0=self.g
        n=self.n[i]
        Q=np.array(self.Q)
        R=self.R
        # predict
        mi_=mi+(-d0*mi-b0*mi*abs(mi)+g0*n**2)*dt
        A=np.array([1+(-d0-2*b0*mi)*dt])
        P_=A*P@A.T+Q
        # update
        C=np.ones((3,))
        G=mi_*C
        K=(P_*C.T)@np.linalg.inv(C*P_@C.T+R)
        mi=mi_+K@(z-G)
        P=(1-K@C)*P_
        self.u_ekf.append(mi)
        self.P=P
        
    
        

if __name__ == '__main__':
    s=9
    navio=Navio(s)
    navio.run()
    # navio.plot_u()
    navio.params()
    # navio.plot_n()
    # navio.plot_z()
    # navio.plot_sensores()
    

