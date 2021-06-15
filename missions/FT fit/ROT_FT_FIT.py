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
propeller.dem_rotation = propeller.max_rotation/5.4

rot   = list()

for i in range(0, steps):
    sim.step()
    rot.append(ship.angular_velocity[2])
    if i > 1000:
        rudder.dem_angle = math.radians(-10)
rot=np.rad2deg(np.array(rot[1000:1200]))
################
# Control Lib  #
################
K  = -max(rot)/np.rad2deg(rudder.dem_angle)
dt = 0.1
t  = np.linspace(0, 200*dt, 200)
T  = np.interp(0.632*max(rot), rot, t)
FT = co.tf([K], [T, 1])

yout, t = co.step(10*FT, t)
FT_str=str(round(K,3))+"/("+str(round(T,3))+"s+1)"
########
# Plot #
########
plt.figure()

plt.plot(t, rot, label="Pydyna")
plt.plot(t, yout, label=FT_str)

plt.xlabel("tempo [s]")
plt.ylabel("velocidade angular [o/s]")
# plt.title("Resposta do Velocidade Angular")
plt.legend()
plt.show()


#pydyna.destroy_simulation(sim)
    