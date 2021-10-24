# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:36:47 2021

@author: lhsca
"""
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

pressed_cells = [(19.0, 74.0), (19.0, 73.0), (19.0, 72.0), (19.0, 71.0), (20.0, 71.0), (20.0, 72.0), (20.0, 74.0), (20.0, 73.0), (55.0, 22.0), (55.0, 23.0), (54.0, 22.0)]
rest_cell = np.zeros((73,116))
for rectangle in pressed_cells:
        y=int(rectangle[0])
        x=int(rectangle[1])
        rest_cell[y][x]=1


fig = plt.figure()
ax = fig.add_subplot(111)
ax.locator_params(nbins=10)
ax.matshow(rest_cell, cmap=cm.binary, extent=[0,30*116,30*73,0])


plt.show()

