import urllib.request
from tkinter import *
from tkinter.tix import *
from PIL import Image, ImageTk

root = Tk()
root.iconbitmap(default='images/icon.png')
root.wm_title('NACMM Mission Manager')
frame = Frame(width="500",height="500")
frame.pack()
swin = ScrolledWindow(frame, width=500, height=500)
swin.pack()
win = swin.window

# imagem
load = Image.open('images/sepetiba.TIF')
background = ImageTk.PhotoImage(load)
bg_width, bg_height = background.width(), background.height()
topo = Canvas(width=bg_width, height=bg_height)
topo.create_image(0,0, image=background, anchor='nw')
topo.pack()

def show():
    print("hi")

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Commands", menu=filemenu)
filemenu.add_command(label="Say hi", command=show)


root.mainloop()