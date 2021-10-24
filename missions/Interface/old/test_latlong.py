import numpy as np
from pyproj import Proj
import utm
from math import pi, cos, sqrt, sin, tan

origem = (-22.936561,-43.831941)
shapemeters=(5804+17134,4647+12131)

pos_latlong = (-22.94417172,-43.82658012)
pos_xy = (542,-846)

# func latlong

def latlong2local(lat,long):
    deg2rad=pi/180
    dfa=6378137
    dfb=6356752
    dftanlat2 = tan(lat*deg2rad)**2
    dfRadius = dfb*sqrt(1+dftanlat2)/sqrt(dfb**2/dfa**2+dftanlat2)
    dXArcDeg  = (long - origem[1]) * deg2rad
    x = dfRadius * sin(dXArcDeg)*cos(lat*deg2rad)
    dYArcDeg  = (lat - origem[0]) * deg2rad
    y = dfRadius * sin(dYArcDeg)
    return x, y

xp, yp = latlong2local(pos_latlong[0],pos_latlong[1])

p0 = utm.from_latlon(origem[0],origem[1])
p1 = utm.from_latlon(pos_latlong[0],pos_latlong[1])
x = p1[0]-p0[0]
y = p1[1]-p0[1]

print("Ponto de teste=", pos_xy[0],pos_xy[1])
print("Ponto de teste (func)=", xp,yp)
print("Ponto de teste (utm)=", x,y)


params={}
with open("itaguai.info", 'r') as f:
    text = f.readlines()
    for line in text:
        p = line.split(' ')
        p[:] = [x for x in p if x]
        params[p[0]]=float(p[2])

p0 = utm.from_latlon(params['lat_south'],params['lon_west'])
p1 = utm.from_latlon(params['lat_north'],params['lon_east'])

x0, y0 = latlong2local(params['lat_south'],params['lon_west'])
x1, y1 = latlong2local(params['lat_north'],params['lon_east'])

print("shape original = ", shapemeters)
print("shape com func", [x1-x0, y1-y0])
print("shape com utm = ", [p1[0]-p0[0],p1[1]-p0[1]])



# com pyproj
# p = Proj(proj='utm', zone=23, ellps='WGS84', preserve_units=False, south=True)
# x0,y0 = p(origem[0],origem[1])
# x1,y1 = p(pos_latlong[0],pos_latlong[1])
# print(x0-x1,y0-y1)

# com utm
# p0 = utm.from_latlon(origem[0],origem[1])
# p1 = utm.from_latlon(pos_latlong[0],pos_latlong[1])
# x = p1[0]-p0[0]
# y = p1[1]-p0[1]
# print(x,y)

# p0 = utm.from_latlon(origem[0],origem[1])
# latlong = utm.to_latlon(p0[0]-pos_xy[0],p0[1]-pos_xy[1],23,"K")
# print(latlong[0],latlong[1])





