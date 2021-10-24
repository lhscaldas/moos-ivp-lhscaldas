import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk



class NACMMsetup(ttk.Frame):
    def __init__(self, container, chart, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.origin=(3000,2020)
        self.shape=(10488,7551)
        
        # GET position
        self.pos_flag=tk.IntVar()
        self.pos_flag.set(0)
        self.last_x=0
        self.last_y=0

    
        # main canvas
        self.canvas = tk.Canvas(self)
        
        # chart
        self.chart = chart
        self.chart_panel=tk.Canvas(self.canvas, width=1600, height=900)
        
        # side panel
        self.side_panel=tk.Canvas(self.canvas)
        

    def load_chart(self):
        self.chart_panel.create_image(0,0, image=self.chart, anchor='nw')
        xscrollbar = ttk.Scrollbar(self.chart_panel, orient="horizontal", command=self.chart_panel.xview)
        yscrollbar = ttk.Scrollbar(self.chart_panel, orient="vertical", command=self.chart_panel.yview)
        xscrollbar.pack(side="bottom", fill="both")
        yscrollbar.pack(side="right", fill="both")
        self.chart_panel.configure(xscrollcommand=xscrollbar.set)
        self.chart_panel.configure(yscrollcommand=yscrollbar.set)
        self.chart_panel.configure(width=self.shape[0])
        self.chart_panel.configure(width=self.shape[1])
        self.chart_panel.configure(scrollregion = self.chart_panel.bbox("all"))

    def print_pos(self,event):
        if self.pos_flag.get()==1:
            self.last_x = self.chart_panel.canvasx(event.x)
            self.last_y = self.chart_panel.canvasy(event.y)
        else:
            pass
    
    def go_to_origin(self):
        self.chart_panel.xview_moveto(self.origin[0]/self.shape[0])
        self.chart_panel.yview_moveto(self.origin[1]/self.shape[1])



    def populate(self):
        # main canvas
        self.canvas.pack(side="left", fill="both",expand=True)
        
        # chart panel
        self.chart_panel.pack(side="right", fill="both",expand=True)
        self.chart_panel.bind("<Button-1>", self.print_pos)

        # side panel
        self.side_panel.pack(side="left")
        button_load = tk.Button(self.side_panel, text="Load Chart", width=30, command=lambda : self.load_chart())
        button_load.pack(side="top")
        button_origin = tk.Button(self.side_panel, text="Go to origin", width=30, command=lambda : self.go_to_origin())
        button_origin.pack(side="bottom")
        xlabel = tk.Label(self.side_panel, text = f"x={self.last_x}")
        xlabel.pack(side="bottom")
        ylabel = tk.Label(self.side_panel, text = f"y={self.last_y}")
        ylabel.pack(side="bottom")
        button_pos = tk.Checkbutton(self.side_panel, text="Enable/Disable Position", var=self.pos_flag)
        button_pos.pack(side="bottom")


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1800x900')
    root.title('NACMM Mission Manager')

    chart_path = 'sepetiba.TIF'
    load = Image.open(chart_path)
    chart = ImageTk.PhotoImage(load)

    frame = NACMMsetup(root, chart)
    frame.pack(side="left", fill="both", expand=True)
    frame.populate()
    root.mainloop()

    
    