#!/usr/bin/env python
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

def RangeSensorLogReader(log_file,var,vname):
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

def RealRangeLogReader(log_file,var,vname):
    t = []
    x = []
    with open(log_file, 'r') as f:
        text = f.readlines()
        for line in text[4:]:
            p = line.split(' ')
            p[:] = [x for x in p if x]
            if var in p:
                reports = p[3:-1]
                for report in reports:
                    info=report.split(',')
                    if 'vname='+vname in info:
                        dist = info[1].split('=')
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
    t,x = RangeSensorLogReader(file,"USR_RANGE_REPORT",target)

    plt.plot(t,x,"-",label=f"Radar")
    t,x = RangeSensorLogReader(file,"USL_RANGE_REPORT",target)

    plt.plot(t,x,"-",label=f"Lidar")
    t,x = RealRangeLogReader(file,"CONTACTS_RECAP",target)

    plt.plot(t,x,"--",label=f"Real")
    str = "Distância de " + target + " medida por alfa"
    plt.title(str)
    plt.xlabel("tempo [s]")
    plt.ylabel("distância [m]")
    plt.legend()
    # plt.axis([0,max(t),min(x)*0.8,max(x)*1.2])
    plt.show()


if __name__ == "__main__":
    file='Log/Log.alog'
    target="bravo"
    range_log(file,target)
    target="charlie"
    range_log(file,target)
    # target="delta"
    # range_log(file,target)


