import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk



class NACMMsetup(ttk.Frame):
    def __init__(self, container, chart, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.origin=(3000,2020)
        self.shape=(10488,7551)
        self.container=container
        
        # GET position
        self.pos_flag=tk.IntVar()
        self.pos_flag.set(0)
    
        # main canvas
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="left", fill="both",expand=True)
        
        # sub canvas
        self.chart_panel=tk.Canvas(self.canvas, width=0, height=0)
        self.chart_panel.pack(side="right", fill="both",expand=True)
        self.side_panel=tk.Canvas(self.canvas)
        self.side_panel.pack(side="left")

        # chart panel
        self.chart = chart
        self.chart_panel.bind("<Button-1>", self.print_pos)
        
        # side panel
        self.button_load = tk.Button(self.side_panel, text="Carregar Carta", width=30, command=lambda : self.load_chart())
        self.button_load.grid(column=0, row=1, columnspan=2)
        self.button_origin = tk.Button(self.side_panel, text="Ir para origem", width=30, command=lambda : self.go_to_origin())
        self.button_origin.grid(column=0, row=2, columnspan=2)
        self.button_pos = tk.Checkbutton(self.side_panel, text="capturar posição", var=self.pos_flag)
        self.button_pos.grid(column=0, row=3, columnspan=2)
        self.xlabel = tk.Label(self.side_panel, text = "x= 0")
        self.xlabel.grid(column=0, row=4)
        self.ylabel = tk.Label(self.side_panel, text = "y= 0")
        self.ylabel.grid(column=1, row=4)
        
        

    def load_chart(self):
        self.chart_panel.create_image(0,0, image=self.chart, anchor='nw')
        xscrollbar = ttk.Scrollbar(self.chart_panel, orient="horizontal", command=self.chart_panel.xview)
        yscrollbar = ttk.Scrollbar(self.chart_panel, orient="vertical", command=self.chart_panel.yview)
        xscrollbar.pack(side="bottom", fill="both")
        yscrollbar.pack(side="right", fill="both")
        self.chart_panel.configure(xscrollcommand=xscrollbar.set)
        self.chart_panel.configure(yscrollcommand=yscrollbar.set)
        self.chart_panel.configure(width=self.shape[0])
        self.chart_panel.configure(height=self.shape[1])
        self.chart_panel.configure(scrollregion = self.chart_panel.bbox("all"))
        self.container.geometry('1800x900')
        self.side_panel.configure(height=self.shape[1])

    def print_pos(self,event):
        if self.pos_flag.get()==1:
            x = self.chart_panel.canvasx(event.x)
            y = self.chart_panel.canvasy(event.y)
            self.xlabel.configure(text=f"x= {x}")
            self.ylabel.configure(text=f"y= {y}")
        else:
            pass
    
    def go_to_origin(self):
        self.chart_panel.xview_moveto(self.origin[0]/self.shape[0])
        self.chart_panel.yview_moveto(self.origin[1]/self.shape[1])


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x200')
    root.title('NACMM Mission Manager')

    chart_path = 'sepetiba.TIF'
    load = Image.open(chart_path)
    chart = ImageTk.PhotoImage(load)

    frame = NACMMsetup(root, chart)
    frame.pack(side="left", fill="both", expand=True)
    root.mainloop()

    
    