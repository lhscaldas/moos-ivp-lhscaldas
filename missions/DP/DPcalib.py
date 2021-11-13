import pydyna
import inhousedp
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import pandas as pd
ydyna.create_simulation("PSV4500.p3d")
my_dyna.reset()
my_vessel = my_dyna.vessels['207']
my_thrusters = list(my_vessel.thrusters)
my_vessel.linear_position = [0.0, 0.0, -6.6]
my_vessel.angular_position = [0.0, 0.0, 0.0]
print(my_vessel.linear_position)
print(my_vessel.angular_position)
print(my_thrusters)
my_dp = inhousedp.InhouseDP("/home/lhscaldas/moos-ivp-lhscaldas/missions/DP/PSV4500.p3d", 207)


# my_dyna = pydyna.create_simulation("NACMM_2021.p3d")
# my_dyna.reset()
# my_vessel = my_dyna.vessels['292']
# my_thrusters = list(my_vessel.thrusters)
# my_vessel._set_linear_position([0.0, 0.0, -1.0])
# my_vessel._set_angular_position([0.0, 0.0, 0.0])
# my_vessel._set_linear_velocity([0.0, 0.0, 0.0])
# my_vessel._set_angular_velocity([0.0, 0.0, 0.0])
# print(my_vessel.linear_position)
# print(my_vessel.angular_position)
# print(my_thrusters)
# my_dp = inhousedp.InhouseDP("/home/lhscaldas/moos-ivp-lhscaldas/missions/DP/NACMM_2021.p3d", 292)


# %%
my_dyna.reset()
serie_t_2 = []
serie_x_2 = []
serie_y_2 = []
serie_yaw_2 = []

serie_thrust1 = []
serie_thrust2 = []
# serie_thrust3 = []

serie_speed = []
# my_dp.setgains(inhousedp.Dof.SURGE.value, 1e8, 1e8, 1e8)
my_dp.setreference([10.0, 10.0, np.deg2rad(45)])


# %%
for cycle in range(6000):
    serie_t_2.append(my_dyna.get_time_step() * my_dyna.get_dt())
    serie_x_2.append(my_vessel.linear_position[0])
    serie_y_2.append(my_vessel.linear_position[1])
    serie_yaw_2.append(my_vessel.angular_position[2])

    serie_speed.append(my_vessel.linear_velocity[0])

    serie_thrust1.append(my_vessel.thrusters[my_thrusters[0]].dem_rotation)
    serie_thrust2.append(my_vessel.thrusters[my_thrusters[1]].dem_rotation)
    # serie_thrust3.append(my_vessel.thrusters[my_thrusters[2]].dem_rotation)
    
    
    


    my_var = my_dp.dostep([
        my_vessel.linear_position[0],
        my_vessel.linear_position[1],
        my_vessel.angular_position[2]
    ])
    for one_thr in my_thrusters:
        my_vessel.thrusters[one_thr].dem_rotation = my_var[one_thr].getDemandedRps()
        my_vessel.thrusters[one_thr].dem_pitch = my_var[one_thr].getDemandedPod()
        my_vessel.thrusters[one_thr].dem_angle = my_var[one_thr].getDemandedAzimuth()
    
    my_dyna.step()


# %%

print

plt.figure()
plt.plot(serie_t_2,serie_thrust1,label="thrust 0")
plt.plot(serie_t_2,serie_thrust2,label="thrust 1")
# plt.plot(serie_t_2,serie_thrust3,"thrust 3")
plt.legend()
plt.xlabel("tempo [s]")
plt.ylabel("rotação [rps]")
plt.show()

# print(np.rad2deg(serie_yaw_2[-1]))
# plt.figure()
# plt.plot(serie_x_2,serie_y_2,"--")
# plt.scatter(serie_x_2[0],serie_y_2[0],s=200,c='red',label="início")
# plt.scatter(serie_x_2[-1],serie_y_2[-1],s=200,c='green',label="final")
# plt.legend()
# plt.xlabel("x [m]")
# plt.ylabel("y [m]")
# plt.axis("equal")
# plt.show()

# plt.figure()
# plt.plot(serie_t_2,serie_speed,"")
# plt.xlabel("tempo [s]")
# plt.ylabel("velocidade [m/s]")
# plt.show()

# plt.figure()
# plt.plot(serie_t_2,serie_x_2,label="x")
# plt.plot(serie_t_2,serie_y_2,label="y")
# plt.legend()
# plt.xlabel("tempo [s]")
# plt.ylabel("distância [m]")
# plt.show()


plt.rcParams["figure.figsize"] = (16,8)
data = pd.DataFrame({'t': serie_t_2, 'px': serie_x_2, 'py': serie_y_2, 'yaw': serie_yaw_2})
fig, (ax1) = plt.subplots(1, 1)
ax1.set_aspect('equal')

Path = mpath.Path
path_data = [
    (Path.MOVETO, [0.0, -0.5]),
    (Path.LINETO, [-0.35, -0.5]),
    (Path.LINETO, [-0.5, -0.4]),
    (Path.LINETO, [-0.5, -0.35]),
    (Path.LINETO, [-0.5, 0.3]),
    (Path.CURVE4, [-0.5, 0.5]),
    (Path.CURVE4, [0.5, 0.5]),
    (Path.LINETO, [0.5, 0.3]),
    (Path.LINETO, [0.5, 0.3]),
    (Path.LINETO, [0.5, -0.35]),
    (Path.LINETO, [0.5, -0.4]),
    (Path.LINETO, [0.35, -0.5]),
    (Path.CLOSEPOLY, [0.0, -0.5])
]

codes, verts = zip(*path_data)
ship = [[x[0] * my_vessel.breadth, x[1] * my_vessel.length] for x in verts]

for key, t in enumerate(data['t']):
    if (key % 100) == 0:
        alpha = data['yaw'][key] - math.pi/2
        item = [[x[0] * math.cos(alpha) - x[1] * math.sin(alpha), 
            x[0] * math.sin(alpha) + x[1] * math.cos(alpha)] for x in ship]
        item = [[x[0] + data['px'][key], x[1] + data['py'][key]] for x in item]

        path = mpath.Path(item, codes)
        patch = mpatches.PathPatch(path, facecolor='gray', alpha=0.4)
        ax1.add_patch(patch)

ax1.plot(data['px'], data['py'])

ax1.set_title("Position")
ax1.set_xlabel("X (m)")
ax1.set_ylabel("Y (m)")

ax1.set_ylim(data['py'].min() - my_vessel.length, data['py'].max() + my_vessel.length)
ax1.set_xlim(data['px'].min() - my_vessel.length, data['px'].max() + my_vessel.length)

plt.show()



# %%
