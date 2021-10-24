# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:36:47 2021

@author: lhsca
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

pressed_cells = [(19.0, 74.0), (19.0, 73.0), (19.0, 72.0), (19.0, 71.0), (20.0, 71.0), (20.0, 72.0), (20.0, 74.0), (20.0, 73.0), (55.0, 22.0), (55.0, 23.0), (54.0, 22.0)]
rest_cell = np.zeros((73,116))
for rectangle in pressed_cells:
        y=int(rectangle[0])
        x=int(rectangle[1])
        rest_cell[y][x]=1


fig = plt.figure("Células Restritas")
ax = fig.add_subplot(111)
ax.locator_params(nbins=10)
ax.matshow(rest_cell, cmap=cm.binary, extent=[0,30*116,30*73,0])


plt.axis("equal")

plt.show(block=False)

plt.figure("Pontos Restritos")

x=np.linspace(0,116*30,116*2+1)
y=np.linspace(-73*30,0,73*2+1)
xv, yv = np.meshgrid(x, y)
plt.scatter(xv,yv,c="k",s=0.01)

X=np.linspace(0,116*30,116+1)
Y=np.linspace(-73*30,0,73+1)
Xv, Yv = np.meshgrid(X, Y)
plt.scatter(Xv,Yv,c="k",s=1)

rest = []
x_list = []
y_list = [] 
for cell in pressed_cells:
        i=cell[1]
        j=cell[0]
        xr=np.linspace(30*i,30*(i+1),3)
        yr=np.linspace(-30*j,-30*(j+1),3)
        Xr, Yr = np.meshgrid(xr, yr)
        rest.append([Xr,Yr])
        x_list.extend(list(xr))
        y_list.extend(list(yr))
rest_point_list = [x_list,y_list]
print(rest_point_list)       

for cell in rest:
    Xr=cell[0]
    Yr=cell[1]
    plt.scatter(Xr,Yr,c="r",s=2)
    
      
plt.show(block=False)

d=20
plt.axis([0-d,116*30+d,-73*30-d,0+d])

input()