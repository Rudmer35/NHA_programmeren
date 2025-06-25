from tkinter import *

def doe_niets():
    filewin=Toplevel(root)
    button = Button(filewin, text="Doe niets knop")
    button.pack()

root = Tk()
root.geometry("640x480")
menubar = Menu(root)
bestandsmenu = Menu(menubar, tearoff=0)
bestandsmenu.add_command(label="Nieuw", command=doe_niets)
bestandsmenu.add_command(label="Open", command=doe_niets)
bestandsmenu.add_command(label="Opslaan", command=doe_niets)
bestandsmenu.add_command(label="Opslaan als...", command=doe_niets)
bestandsmenu.add_command(label="Afsluiten", command=doe_niets)
bestandsmenu.add_separator()
bestandsmenu.add_command(label="Stoppen", command=doe_niets)
menubar.add_cascade(label="Bestand", menu=bestandsmenu)
root.config(menu=menubar)

root.mainloop()
