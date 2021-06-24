from LogReader import LogReader
import matplotlib.pyplot as plt

file='missions/sensores_2/MOOSLog_24_6_2021_____16_56_42/MOOSLog_24_6_2021_____16_56_42.alog'
def hdg_log(var):
    t, x=LogReader(file,var)
    plt.plot(t[1:],x[1:],label=var)
    plt.xlabel("tempo [s]")
    plt.ylabel("[o]")

def spd_log(var):
    t, x=LogReader(file,var)
    plt.plot(t[1:],x[1:],label=var)
    plt.xlabel("tempo [s]")
    plt.ylabel("[m/s]")

plt.figure(1)
hdg_log("DESIRED_HEADING")
hdg_log("REAL_HEADING")
plt.legend()
plt.title("PID de rumo")
plt.axis([0, 1300, 0, 400])
plt.show()

plt.figure(2)
hdg_log("GYRO_HEADING")
hdg_log("IMU_HEADING")
plt.title("Sensores de rumo")
plt.legend()
plt.axis([0, 1300, 0, 400])
plt.show()

plt.figure(3)
spd_log("DESIRED_SPEED")
spd_log("REAL_SPEED")
plt.legend()
plt.title("PID de velocidade")
plt.axis([0, 1300, -1, 7])
plt.show()

plt.figure(4)
spd_log("DVL_SPEED")
spd_log("IMU_SPEED")
spd_log("GPS_SPEED")
plt.legend()
plt.title("Sensores de velocidade")
plt.axis([0, 1300, -1, 7])
plt.show()



