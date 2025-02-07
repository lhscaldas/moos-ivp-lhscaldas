from os import name
import matplotlib.pyplot as plt

def LogReader(log_file,var):
    t = []
    x = []
    with open(log_file, 'r') as f:
        text = f.readlines()
        for line in text[4:]:
            p = line.split(' ')
            p[:] = [x for x in p if x]
            if var in p:
              t.append(float(p[0]))
              x.append(float(p[-2]))
    return t, x

def RangeLogReader(log_file,var,vname):
    t = []
    x = []
    with open(log_file, 'r') as f:
        text = f.readlines()
        for line in text[4:]:
            p = line.split(' ')
            p[:] = [x for x in p if x]
            if var in p:
                report = p[3]
                info=report.split(',')
                target=info[2].split('=')
                dist = info[1].split('=')
                if target[1] == vname:
                    t.append(float(p[0])) 
                    x.append(float(dist[1]))
    return t, x

def hdg_log(file,var):
    t, x=LogReader(file,var)
    plt.plot(t[1:],x[1:],label=var)
    plt.xlabel("tempo [s]")
    plt.ylabel("[o]")

def spd_log(file,var):
    t, x=LogReader(file,var)
    plt.plot(t[1:],x[1:],label=var)
    plt.xlabel("tempo [s]")
    plt.ylabel("[m/s]")

def range_log(file,target):
    plt.figure()
    t,x = RangeLogReader(file,"USR_RANGE_REPORT",target)
    plt.plot(t,x,label="Radar")
    t,x = RangeLogReader(file,"USL_RANGE_REPORT",target)
    plt.plot(t,x,label="Lidar")
    t,x = RangeLogReader(file,"USR_RANGE_REPORT_GT",target)
    plt.plot(t,x,"--",label="Real")
    str = "Distância de " + target + " medida por alfa"
    plt.title(str)
    plt.xlabel("tempo [s]")
    plt.ylabel("distância [m]")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    file='missions/shoreside/Log/Log.alog'
    target="bravo"
    range_log(file,target)
    target="charlie"
    range_log(file,target)
    target="delta"
    range_log(file,target)




# plt.figure(1)
# hdg_log("DESIRED_HEADING")
# hdg_log("REAL_HEADING")
# plt.legend()
# plt.title("PID de rumo")
# plt.axis([0, 1300, 0, 400])
# plt.show()

# plt.figure(2)
# hdg_log("GYRO_HEADING")
# hdg_log("IMU_HEADING")
# plt.title("Sensores de rumo")
# plt.legend()
# plt.axis([0, 1300, 0, 400])
# plt.show()

# plt.figure(3)
# spd_log("DESIRED_SPEED")
# spd_log("REAL_SPEED")
# plt.legend()
# plt.title("PID de velocidade")
# plt.axis([0, 1300, -1, 7])
# plt.show()

# plt.figure(4)
# spd_log("DVL_SPEED")
# spd_log("IMU_SPEED")
# spd_log("GPS_SPEED")
# plt.legend()
# plt.title("Sensores de velocidade")
# plt.axis([0, 1300, -1, 7])
# plt.show()



