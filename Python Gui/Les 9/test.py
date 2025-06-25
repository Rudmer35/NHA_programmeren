from tkinter import *

def sel():
    selectie = 'waarde = ' + str(var.get())
    lbl_scale.config(text=selectie)

root=Tk()
var=DoubleVar()
scale= Scale(root, variable=var)
scale.pack(anchor=CENTER)

btn_haal_waarde = Button(root, text='Haal waarde van Scale', command=sel)
btn_haal_waarde.pack(anchor=CENTER)

lbl_scale = Label(root)
lbl_scale.pack()

root.mainloop()