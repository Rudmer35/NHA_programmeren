from tkinter import *
from tkinter import messagebox

root = Tk()
root.config(bg='yellow')
root.geometry('320x240')
root.title='Rekenmachine'

getal1 = IntVar()
getal2 = IntVar()
rekenteken = StringVar()
antwoord = StringVar()

def show_answer():
    if rekenteken.get() == '+':
        antwoord=getal1.get() + getal2.get()
    elif rekenteken.get() == '-':
        antwoord=getal1.get() - getal2.get()
    elif rekenteken.get() == '*':
        antwoord = getal1.get() * getal2.get()
    elif rekenteken.get() == '/':
        antwoord = getal1.get() / getal2.get()
    else:
        antwoord = 'Geen correct rekenteken'
    messagebox.showinfo(title='Antwoord', message=antwoord)

frame = Frame(root, bg='grey', height=200)
frame.pack()

Label(frame, width=30, text='Geef twee getallen en een rekenteken')
Entry(frame, width=30, textvariable=getal1).pack()
Entry(frame, width=30, textvariable=getal2).pack()
Entry(frame, width=30, textvariable=rekenteken).pack()
Button(frame, width=25, text='Uitrekenen', command=show_answer).pack()

root.mainloop()