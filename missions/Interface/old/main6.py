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

        # Pressionar células
        self.pressed_cells = list()
        self.rectangles = list()
    
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
        self.chart_panel.bind("<Button-1>", self.mouse1_callback)
        
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

    def mouse1_callback(self, event):
        if self.pos_flag.get()==1:
            self.print_pos(event)
        else:
            self.choose_cell(event)
    
    def print_pos(self,event):
        x = self.chart_panel.canvasx(event.x)
        y = self.chart_panel.canvasy(event.y)
        self.xlabel.configure(text=f"x= {x}")
        self.ylabel.configure(text=f"y= {y}")

    def go_to_origin(self):
        self.chart_panel.xview_moveto(self.origin[0]/self.shape[0])
        self.chart_panel.yview_moveto(self.origin[1]/self.shape[1])

    def choose_cell(self, event):
        m_cells = 250
        n_cells = 250
        height = self.shape[1]
        width = self.shape[0]
        x = self.chart_panel.canvasx(event.x)
        y = self.chart_panel.canvasy(event.y)
        i = (y * m_cells) // height + 1
        j = (x * n_cells) // width + 1
        if (i, j) not in self.pressed_cells:
            print(f"Célula pressionada: ({i}, {j})")
            self.pressed_cells.append((i, j))
            x1 = (j-1) * width / n_cells
            y1 = (i-1) * height / m_cells
            x2 = j * width / n_cells
            y2 = i * height / m_cells
            rectangle = self.chart_panel.create_rectangle(x1, y1, x2, y2, width=1, fill="black", stipple="gray50")
            self.rectangles.append(rectangle)
        else:
            print(f"Célula despressionada: ({i}, {j})")
            rectangle_id = self.pressed_cells.index((i, j))
            self.pressed_cells.remove((i, j))
            self.chart_panel.delete(self.rectangles[rectangle_id])
            self.rectangles.pop(rectangle_id)

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

    
    