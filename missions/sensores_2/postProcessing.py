from LogReader import LogReader
import matplotlib.pyplot as plt

def hdg_log(var):
    t, x=LogReader('missions/sensores_2/testeLog.txt',var)
    plt.plot(t[1:],x[1:],label=var)
    plt.xlabel("tempo [s]")
    plt.ylabel("")

plt.figure(1)
hdg_log("DESIRED_HEADING")
hdg_log("NAV_HEADING")
plt.legend()
plt.show()