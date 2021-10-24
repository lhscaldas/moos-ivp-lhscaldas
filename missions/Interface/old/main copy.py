import tkinter as tk
from tkinter import Label, ttk, messagebox
from tkinter.constants import DOTBOX
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from pathlib import Path
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
import matplotlib.pyplot as plt
from matplotlib import cm
from math import pi, cos, sqrt, sin, tan, asin



class NACMMsetup(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.originpixel=[7834,2090]
        self.originlatlong=[-22.93998301,-43.98827046] # [-22.936561,-43.831941]
        self.shapepixel=(10488,75510)
        self.shapemeters=(2298, 16778) #(5804+17134,4647+12131)(22938, 16778)
        self.container=container
        
        # Mouse function
        self.click_flag=tk.IntVar()
        self.click_flag.set(0)

        # Pressionar células
        self.pressed_cells = list()
        self.rectangles = list()

        # Restrições
        self.rest_cell = np.zeros((73,116))
        self.rest_point_list = [] 
        
        # Inicio e fim
        self.begin = [-100,0]
        self.begin_marker = []
        self.end = [-100,0]
        self.end_marker = []

        # selecionar origem
        self.latstring=tk.StringVar(value=str(self.originlatlong[0]))
        self.longstring=tk.StringVar(value=str(self.originlatlong[1]))
    
        # main canvas
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="left", fill="both",expand=True)
        
        # sub canvas
        self.chart_panel=tk.Canvas(self.canvas, width=0, height=0)
        self.chart_panel.pack(side="right", fill="both",expand=True)
        self.side_panel=tk.Canvas(self.canvas)
        self.side_panel.pack(side="left")

        # chart panel
        self.chart = 0
        self.chart_panel.bind("<Button-1>", self.mouse1_callback)
        
        # side panel
        self.button_load = tk.Button(self.side_panel, text="Carregar Carta", width=30, command=lambda : self.load_chart())
        self.button_load.grid(column=0, row=0, columnspan=2)

        self.latorigemlabel=tk.Label(self.side_panel, text = "Lat_origem = ")
        self.latorigemlabel.grid(column=0, row=1)
        self.latorigem=tk.Entry(self.side_panel, textvariable=self.latstring)
        self.latorigem.grid(column=1, row=1)

        self.longorigemlabel=tk.Label(self.side_panel, text = "Long_origem = ")    
        self.longorigemlabel.grid(column=0, row=2)
        self.longorigem=tk.Entry(self.side_panel, textvariable=self.longstring)
        self.longorigem.grid(column=1, row=2)   

        self.button_origin = tk.Button(self.side_panel, text="Ir para origem", width=30, command=lambda : self.go_to_origin())
        self.button_origin.grid(column=0, row=3, columnspan=2)

        self.mouselabel = tk.Label(self.side_panel, text = "Função do clique:")
        self.mouselabel.grid(column=0, row=4, columnspan=2)
        self.mouse0 = tk.Radiobutton(self.side_panel, text="capturar posição", var=self.click_flag, value=0)
        self.mouse0.grid(column=0, row=5, columnspan=2)
        self.mouse1 = tk.Radiobutton(self.side_panel, text="selecionar célula", var=self.click_flag, value=1)
        self.mouse1.grid(column=0, row=6, columnspan=2)
        self.mouse2 = tk.Radiobutton(self.side_panel, text="ponto inicial", var=self.click_flag, value=2)
        self.mouse2.grid(column=0, row=7, columnspan=2)
        self.mouse3 = tk.Radiobutton(self.side_panel, text="ponto final", var=self.click_flag, value=3)
        self.mouse3.grid(column=0, row=8, columnspan=2)
    
        
        self.button_printcell = tk.Button(self.side_panel, text = "Atualizar restrição", width=30, command=lambda : self.gen_restriction())
        self.button_printcell.grid(column=0, row=9, columnspan=2)

        self.button_printcell = tk.Button(self.side_panel, text = "Imprimir células", width=30, command=lambda : self.plot_cells())
        self.button_printcell.grid(column=0, row=10, columnspan=2)

        self.button_printcell = tk.Button(self.side_panel, text = "Imprimir pontos", width=30, command=lambda : self.plot_dots())
        self.button_printcell.grid(column=0, row=11, columnspan=2)


        self.poslabel = tk.Label(self.side_panel, text = "Posição do clique:")
        self.poslabel.grid(column=0, row=12, columnspan=2)

        self.xlabel = tk.Label(self.side_panel, text = "x= 0")
        self.xlabel.grid(column=0, row=13)
        self.ylabel = tk.Label(self.side_panel, text = "y= 0")
        self.ylabel.grid(column=1, row=13)
        self.latlabel = tk.Label(self.side_panel, text = "Lat= 0")
        self.latlabel.grid(column=0, row=14)
        self.longlabel = tk.Label(self.side_panel, text = "Long= 0")
        self.longlabel.grid(column=1, row=14)
        
    def origem_callback(self):
        self.originlatlong[0]=float(self.latstring.get())
        self.originlatlong[1]=float(self.longstring.get())
        

    def load_chart(self):
        filepath = Path(askopenfilename())
        load = Image.open(filepath)
        # filename = "itaguai.tif" # para debug
        # load = Image.open(filename) # para debug
        self.chart = ImageTk.PhotoImage(load)
        self.shapepixel = (self.chart.width(),self.chart.height())
        self.chart_panel.create_image(0,0, image=self.chart, anchor='nw')
        xscrollbar = ttk.Scrollbar(self.chart_panel, orient="horizontal", command=self.chart_panel.xview)
        yscrollbar = ttk.Scrollbar(self.chart_panel, orient="vertical", command=self.chart_panel.yview)
        xscrollbar.pack(side="bottom", fill="both")
        yscrollbar.pack(side="right", fill="both")
        self.chart_panel.configure(xscrollcommand=xscrollbar.set)
        self.chart_panel.configure(yscrollcommand=yscrollbar.set)
        self.chart_panel.configure(width=self.shapepixel[0])
        self.chart_panel.configure(height=self.shapepixel[1])
        self.chart_panel.configure(scrollregion = self.chart_panel.bbox("all"))
        self.container.geometry('1800x900')
        self.side_panel.configure(height=900)
        self.set_origin()
        # self.go_to_origin() # para debug
        

    def mouse1_callback(self, event):
        if self.click_flag.get()==0:
            self.print_pos(event)
        elif self.click_flag.get()==1:
            self.choose_cell(event)
        elif self.click_flag.get()==2:
            self.get_begin(event)
        elif self.click_flag.get()==3:
            self.get_end(event)
    
    def get_begin(self,event):
        x_, y_ = self.get_click_pos(event)
        x = (x_//15)*15
        y = (y_//15)*15
        if x_ % 15 > 7.5:
            x +=15
        if y_ % 15 > 7.5:
            y +=15
        self.begin=[x,y]
        print("Ponto inicial:",self.begin)
        xp, yp = self.meters2pixel(x,y)
        d = 5
        x1, y1 = (xp - d), (yp - d)
        x2, y2 = (xp + d), (yp + d)
        if len(self.begin_marker)==1:
            self.chart_panel.delete(self.begin_marker[0])
            self.begin_marker = []
        begin_dot = self.chart_panel.create_oval(x1, y1, x2, y2, fill="green")
        self.begin_marker.append(begin_dot)

    def get_end(self,event):
        x_, y_ = self.get_click_pos(event)
        x = (x_//15)*15
        y = (y_//15)*15
        if x_ % 15 > 7.5:
            x +=15
        if y_ % 15 > 7.5:
            y +=15
        self.end=[x,y]
        print("Ponto final:",self.end)
        xp, yp = self.meters2pixel(x,y)
        d = 5
        x1, y1 = (xp - d), (yp - d)
        x2, y2 = (xp + d), (yp + d)
        if len(self.end_marker)==1:
            self.chart_panel.delete(self.end_marker[0])
            self.end_marker = []
        end_dot = self.chart_panel.create_oval(x1, y1, x2, y2, fill="red")
        self.end_marker.append(end_dot)



    def get_click_pos(self,event):
        x = self.chart_panel.canvasx(event.x)
        y = self.chart_panel.canvasy(event.y)
        xm, ym = self.pixel2meters(x,y)
        return xm,ym

    def print_pos(self,event):
        xm,ym = self.get_click_pos(event)
        self.xlabel.configure(text=f"x= {round(xm,2)}")
        self.ylabel.configure(text=f"y= {round(ym,2)}")
        lat, long = self.local2latlong(xm,ym)
        self.latlabel.configure(text=f"Lat= {round(lat,4)}")
        self.longlabel.configure(text=f"long= {round(long,4)}")

    def go_to_origin(self):
        self.origem_callback()
        self.chart_panel.xview_moveto(self.originpixel[0]/self.shapepixel[0])
        self.chart_panel.yview_moveto(self.originpixel[1]/self.shapepixel[1])

    def gen_restriction(self):
        self.rest_cell=np.zeros((73,116))
        for rectangle in self.pressed_cells:
            y=int(rectangle[0])
            x=int(rectangle[1])
            self.rest_cell[y][x]=1

        x_list = []
        y_list = [] 
        for cell in self.pressed_cells:
                i=cell[1]
                j=cell[0]
                xr=np.linspace(30*i,30*(i+1),3)
                yr=np.linspace(-30*j,-30*(j+1),3)
                x_list.extend(list(xr))
                y_list.extend(list(yr))
        self.rest_point_list = [x_list,y_list]
        print(self.rest_point_list)

    def choose_cell(self, event):
        dxm = 30 # metros
        dym = 30 # metros
        dxp = dxm*self.shapepixel[0]/self.shapemeters[0]
        dyp = dym*self.shapepixel[1]/self.shapemeters[1]
        n_cells = int(self.shapepixel[0]/dxp)
        m_cells = int(self.shapepixel[1]/dyp)  
        height = self.shapepixel[1]
        width =  self.shapepixel[0]
        first_cell = ((self.originpixel[1] * m_cells) // height + 1, (self.originpixel[0] * n_cells) // width + 1)
        x = self.chart_panel.canvasx(event.x)
        y = self.chart_panel.canvasy(event.y)
        i = (y * m_cells) // height + 1
        j = (x * n_cells) // width + 1
        i_local = i - first_cell[0] -1
        j_local = j - first_cell[1] -1
        if (i_local, j_local) not in self.pressed_cells:
            self.pressed_cells.append((i_local, j_local))
            x1 = (j-1) * width / n_cells
            y1 = (i-1) * height / m_cells
            x2 = j * width / n_cells
            y2 = i * height / m_cells
            rectangle = self.chart_panel.create_rectangle(x1, y1, x2, y2, width=1, fill="black", stipple="gray50")
            self.rectangles.append(rectangle)
        else:
            rectangle_id = self.pressed_cells.index((i_local, j_local))
            self.pressed_cells.remove((i_local, j_local))
            self.chart_panel.delete(self.rectangles[rectangle_id])
            self.rectangles.pop(rectangle_id)

    def plot_cells(self):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Células Restritas')
        ax.matshow(self.rest_cell, cmap=cm.binary, extent=[0,30*116,-30*73,0])
        plt.title('Células Restritas')
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()

    def plot_dots(self):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Pontos Restritos')

        x=np.linspace(0,116*30,116*2+1)
        y=np.linspace(-73*30,0,73*2+1)
        xv, yv = np.meshgrid(x, y)
        ax.scatter(xv,yv,c="k",s=0.01)

        X=np.linspace(0,116*30,116+1)
        Y=np.linspace(-73*30,0,73+1)
        Xv, Yv = np.meshgrid(X, Y)
        ax.scatter(Xv,Yv,c="k",s=1)

        rest = []
        x_list = []
        y_list = [] 
        for cell in self.pressed_cells:
                i=cell[1]
                j=cell[0]
                xr=np.linspace(30*i,30*(i+1),3)
                yr=np.linspace(-30*j,-30*(j+1),3)
                Xr, Yr = np.meshgrid(xr, yr)
                rest.append([Xr,Yr])
                x_list.extend(list(xr))
                y_list.extend(list(yr))
        self.rest_point_list = [x_list,y_list]  
        
        label_flag=0
        for cell in rest:
            Xr=cell[0]
            Yr=cell[1]
            if label_flag==0:
                ax.scatter(Xr,Yr,c="darkorange",s=3,label="pontos restritos")
                label_flag+=1
            else:
                ax.scatter(Xr,Yr,c="darkorange",s=3)

        ax.scatter(self.begin[0],self.begin[1],c="g",s=20,marker='s',label="inicio")
        ax.scatter(self.end[0],self.end[1],c="r",s=20,marker='^',label="fim")

        d=20
        plt.axis([0-d,116*30+d,-73*30-d,0+d])
        plt.title('Pontos Restritos')
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.legend(title='Legenda', bbox_to_anchor=(1.005, 1), loc='upper left')
        plt.show()

    def pixel2meters(self,xp,yp):
        xp0=self.originpixel[0]
        yp0=self.originpixel[1]
        dx=self.shapemeters[0]/self.shapepixel[0]
        dy=self.shapemeters[1]/self.shapepixel[1]
        xm=(xp-xp0)*dx
        ym=(yp-yp0)*dy
        return xm, -ym

    def meters2pixel(self,xm,ym):
        xp0=self.originpixel[0]
        yp0=self.originpixel[1]
        dx=self.shapepixel[0]/self.shapemeters[0]
        dy=self.shapepixel[1]/self.shapemeters[1]
        xp=xp0+xm*dx
        yp=yp0-ym*dy
        return xp, yp

    def set_origin(self):
        params={}
        with open("itaguai.info", 'r') as f:
            text = f.readlines()
            for line in text:
                p = line.split(' ')
                p[:] = [x for x in p if x]
                params[p[0]]=float(p[2])
        xw, ys = self.latlong2local(params['lat_south'],params['lon_west'])
        xe, yn = self.latlong2local(params['lat_north'],params['lon_east'])
        self.shapemeters=(xe-xw,yn-ys)
        dx = self.shapepixel[0]/self.shapemeters[0]
        dy = self.shapepixel[1]/self.shapemeters[1]
        self.originpixel=[-xw*dx,yn*dy]

    def latlong2local(self,lat,long):
        deg2rad=pi/180
        dfa=6378137
        dfb=6356752
        dftanlat2 = tan(lat*deg2rad)**2
        dfRadius = dfb*sqrt(1+dftanlat2)/sqrt(dfb**2/dfa**2+dftanlat2)
        dXArcDeg  = (long - self.originlatlong[1]) * deg2rad
        x = dfRadius * sin(dXArcDeg)*cos(lat*deg2rad)
        dYArcDeg  = (lat - self.originlatlong[0]) * deg2rad
        y = dfRadius * sin(dYArcDeg)
        return x, y

    def local2latlong(self, x, y):
        deg2rad=pi/180
        rad2deg=180/pi
        dfa=6378137
        dfb=6356752
        dftanlat2 = tan(self.originlatlong[0]*deg2rad)**2
        dfRadius = dfb*sqrt(1+dftanlat2)/sqrt(dfb**2/dfa**2+dftanlat2)
        dfYArcRad = asin( y/dfRadius )
        dfYArcDeg = dfYArcRad * rad2deg
        dfXArcRad = asin( x/( dfRadius*cos( self.originlatlong[0]*deg2rad ) ) )
        dfXArcDeg = dfXArcRad * rad2deg
        Lat = dfYArcDeg + self.originlatlong[0]
        Long = dfXArcDeg + self.originlatlong[1]
        return Lat, Long
        


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x200')
    root.title('NACMM Mission Manager')

    frame = NACMMsetup(root)
    # frame.load_chart() # para debug
    frame.pack(side="left", fill="both", expand=True)
    root.mainloop()

    
    