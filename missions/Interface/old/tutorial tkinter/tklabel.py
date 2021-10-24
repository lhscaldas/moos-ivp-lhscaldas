import tkinter as tk
from tkinter import ttk
from pprint import pprint

app = tk.Tk()
logo = tk.PhotoImage(file='tutorial tkinter/logo.png')
labelExample = tk.Label(app, image=logo)
labelExample.pack()
app.mainloop()
