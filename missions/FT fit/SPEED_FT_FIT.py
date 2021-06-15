import pydyna
import math
import matplotlib.pyplot as plt
import numpy as np
import control.matlab as co

####################
# Simulação Pydyna #
####################
sim = pydyna.create_simulation("Navio_L15B4_Conv.p3d")

ship = sim.vessels['207']
rudder = ship.rudders['0']
propeller = ship.thrusters['0']

steps = 2000

ship._set_linear_position([0, 0, 0])
ship._set_linear_velocity([0, 0, 0])

rudder.dem_angle = math.radians(0)
# thrust = 100
# propeller.dem_rotation = np.sqrt(thrust*3.06) # propeller.max_rotation/1
propeller.dem_rotation = propeller.max_rotation/5.4

speed_x = list()

for i in range(0, steps):
    sim.step()
    speed_x.append(ship.linear_velocity[0])

speed_x = np.array(speed_x)
dt = 0.1
t  = np.linspace(0, steps*dt, steps)
################
# Control Lib  #
################
K  = max(speed_x)/propeller.dem_rotation

# sem delay
# T = np.interp(0.632*max(speed_x), speed_x, t)
# FT = co.tf([K], [T, 1])
# FT_str = str(round(K,3))+"/("+str(round(T,3))+"s+1)"
# com delay
t1  = np.interp(0.283*max(speed_x), speed_x, t)
t2  = np.interp(0.632*max(speed_x), speed_x, t)
T = 1.5*(t2-t1)
theta = t2 - T
G = co.tf([K], [T, 1])
num, den = co.pade(theta, n=1)
delay = co.tf(num, den)
FT = G*delay
FT_str = "exp(-"+str(round(theta,2))+"s)*"+str(round(K,2))+"/("+str(round(T,2))+"s+1)"

yout, t = co.step(propeller.dem_rotation*FT, t)
########
# Plot #
########
plt.figure()

plt.plot(t, speed_x, label="Pydyna")
plt.plot(t, yout, label=FT_str)

plt.xlabel("tempo [s]")
plt.ylabel("velocidade [m/s]")
# plt.title("Resposta da Velocidade Linear")
plt.legend()
plt.show()


pydyna.destroy_simulation(sim)

Kp = 0.9*T/K/theta
Ki = theta/0.3
print(f"Kp = {Kp} e Ki = {Ki}")