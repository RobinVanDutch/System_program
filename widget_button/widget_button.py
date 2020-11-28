from tkinter import *
root = Tk()
win = Label(width=30)
vvod = Entry(text='Cod color', width=15)
vvod.insert(0, 'Cod color')
win['text'] = 'Color'
def red():
    vvod.delete(0, END)
    vvod.insert(0, "#ff0000")
    win['text'] = 'red'
def orange():
    vvod.delete(0, END)
    vvod.insert(0, "#FFA500")
    win['text'] = 'orange'
def yellow():
    vvod.delete(0, END)
    vvod.insert(0, "#FFFF00")
    win['text'] = 'yellow'
def green():
    vvod.delete(0, END)
    vvod.insert(0, "#00FF00")
    win['text'] = 'green'
def blue():
    vvod.delete(0, END)
    vvod.insert(0, "#00FFFF")
    win['text'] = 'blue'
def aque():
    vvod.delete(0, END)
    vvod.insert(0, "#0000FF")
    win['text'] = 'aque'
def purple():
    vvod.delete(0, END)
    vvod.insert(0, "#800080")
    win['text'] = 'purple'
b1 = Button(bg='#ff0000', command=red, width=13)
b2 = Button(bg='#FFA500', command=orange, width=13)
b3 = Button(bg='#FFFF00', command=yellow, width=13)
b4 = Button(bg='#00FF00', command=green, width=13)
b5 = Button(bg='#00FFFF', command=blue, width=13)
b6 = Button(bg='#0000FF', command=aque, width=13)
b7 = Button(bg='#800080', command=purple, width=13)
win.pack()
vvod.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
root.mainloop()

