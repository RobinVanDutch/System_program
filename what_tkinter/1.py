from tkinter import *
from tkinter import messagebox
wind = Tk()
num = Entry(width = 25)
num2 = Entry(width = 25)
buttsum = Button(text = "+", width = 20)
buttmin = Button(text = "-", width = 20)
buttpow = Button(text = "*", width = 20)
buttdiv = Button(text = "/", width = 20)
otv = Label(width = 50)

def sum(event):
    try:
        a = float(num.get())
        aa = float(num2.get())
        otv['text'] = (str(a + aa))
    except ValueError:
        messagebox.showerror("нужны цыфры >:(")
def min(event):
    try:
        a = float(num.get())
        aa = float(num2.get())
        otv['text'] = (str(a - aa))
    except ValueError:
        messagebox.showerror("нужны цыфры >:(")
def pow(event):
    try:
        a = float(num.get())
        aa = float(num2.get())
        otv['text'] = (str(a * aa))
    except ValueError:
        messagebox.showerror("нужны цыфры >:(")
def div(event):
    try:
        a = float(num.get())
        aa = float(num2.get())
        otv['text'] = (str(a / aa))
    except ValueError:
        messagebox.showerror("нужны цыфры >:(")
buttsum.bind('<Button-1>', sum)
buttmin.bind('<Button-1>', min)
buttpow.bind('<Button-1>', pow)
buttdiv.bind('<Button-1>', div)
num.pack()
num2.pack()
buttsum.pack()
buttmin.pack()
buttpow.pack()
buttdiv.pack()
otv.pack()
wind.mainloop()