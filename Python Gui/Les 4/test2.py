import sqlite3
import create_db
from tkinter import *
from tkinter import messagebox


#de basis voor het frame
root = Tk()
#hoogte en breedte
root.geometry('250x150')

#de functie die in de event wordt aangeroepen
#let op! de functie moet eerst gedefinieerd zijn
#voordat zij gebruikt kan worden


def show_message():
    gelukt_db = create_db.create_db()
    messagebox.showinfo("Database", gelukt_db)

#frame samenstellen, root is het hoofdelement waar frame
#van afhankelijk is
frame = Frame(root)
#pack is een van de methods, daarnaast heb je ook grid
#en place
frame.pack()
btn_show_message = Button(frame, text ='Toon bericht', command = show_message)
btn_show_message.pack()

root.mainloop()