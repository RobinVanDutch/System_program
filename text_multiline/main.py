from tkinter import *
root = Tk()
def OpenFile():
    a=open(text2.get())
    text.delete(1.0, END)
    text.insert(1.0, a.read())
def SaveFile():
    a = open(text2.get(), 'x')
    a.write(text.get(1.0, END))
    text.delete(1.0, END)

a = Frame()
a.pack()

text2 = Entry(a, width=40)
text2.pack()

Button(a, text="Открыть", command=OpenFile).pack(side=LEFT)
Button(a, text="Сохранить", command=SaveFile).pack(side=LEFT)

aa = Frame()
aa.pack()

text = Text(aa, width=100, height=40, wrap=NONE)
text.pack(side=LEFT)
scroll = Scrollbar(aa, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
scroll2 = Scrollbar(orient=HORIZONTAL, command=text.xview)
scroll2.pack(side=BOTTOM, fill=X)
text.config(xscrollcommand=scroll2.set)

root.mainloop()
