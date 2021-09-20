import tkinter as t
from time import strftime

window = t.Tk()
window.title('DIGITAL CLOCK')

box = t.Label(window, bg="black", fg="teal", font=("Calibri", 90))
box.pack()

def time():
    current_time = strftime('%H:%M:%S %p')
    box.config(text=current_time)
    box.after(1000, time)

time()
t.mainloop()
