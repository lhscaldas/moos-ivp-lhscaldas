from enum import Enum
from math import sin, cos, pi
from py4j.java_collections import ListConverter
from py4j.java_gateway import JavaGateway

class Dof(Enum):
    SURGE = 0
    SWAY  = 1
    YAW   = 2

class Reference:
    def __init__(self):
        self.reference = [0.0, 0.0, 0.0]
        self.position = [0.0, 0.0, 0.0]
        
    def setreference(self, reference):
        self.reference = reference
        while self.reference[2] <= -pi:
            self.reference[2] += 2*pi;
        while self.reference[2] > pi:
            self.reference[2] -= 2*pi;

    def setposition(self, position):
        self.position = position
        while self.position[2] <= -pi:
            self.position[2] += 2*pi;
        while self.position[2] > pi:
            self.position[2] -= 2*pi;

    def getlocalerror(self):
        error = []
        for i in range(3):
            error.append(self.reference[i] - self.position[i])
        
        return [
            error[0]*cos(self.position[2]) + error[1]*sin(self.position[2]),
            -error[0]*sin(self.position[2]) + error[1]*cos(self.position[2]),
            error[2]
        ]
                

class InhouseDP:
    def __init__(self, p3dpath, vesselid):
        self.listconverter = ListConverter()
        self.gateway = JavaGateway()
        self.gateway.load(p3dpath)
        #self.gateway.load()
        self.reference = Reference()
        self.force = self.gateway.new_array(self.gateway.jvm.double, 3)
        self.dofs = self.gateway.jvm.java.util.BitSet(3)
        self.dofs.set(0)
        self.dofs.set(1)
        self.dofs.set(2)
        self.allocation = self.gateway.getAllocation()
        self.pid = self.gateway.getPIDFromP3D(vesselid)
        self.notch = self.gateway.getFilterFromP3D(vesselid)
        self.thrusters = self.gateway.getThrustersFromP3D(vesselid)
        self.jthrusterscollection = self.listconverter.convert(self.thrusters.values(), self.gateway._gateway_client)
        maxforce = [0] * 3
        for value in self.thrusters.values():
            f = value.getMaxForce()
            for d in Dof:
                maxforce[d.value] += f[d.value]

        for d in Dof:
            self.pid[d.value].setAntiWindup(-maxforce[d.value], maxforce[d.value])

    def setreference(self, reference):
        self.reference.setreference(reference)

    def setgains(self, dof, kp, ki, kd):
        self.pid[dof].setControlGains(kp, ki, kd)

    def dostep(self, position):
        self.reference.setposition(position)
        error = self.reference.getlocalerror()

        for i in range(3):
            errorf = self.notch[i].nextState(error[i])
            self.force[i] = self.pid[i].nextState(errorf)

        self.allocation.allocate(self.dofs, self.force, self.jthrusterscollection)

        return self.thrusters
