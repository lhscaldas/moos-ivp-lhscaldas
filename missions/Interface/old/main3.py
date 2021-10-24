import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

load = Image.open('images/sepetiba.TIF')
background = ImageTk.PhotoImage(load)
bg_width, bg_height = background.width(), background.height()
canvas.create_image(0,0, image=background, anchor='nw')
canvas.pack()


scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

# for i in range(50):
#     ttk.Label(scrollable_frame, text="Sample scrolling label").pack()

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()