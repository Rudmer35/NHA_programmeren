from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry('500x300')
root.title('Selecteer persoon')

voor_naam = StringVar()
tussen_voegsel = StringVar()
achter_naam = StringVar()
mo_biel = StringVar()
zoek = StringVar()

def database():

    if achter_naam.get() == "":
        messagebox.ERROR('Error','Geen achternaam ingevuld')
        return FALSE
    else:
        try:
            voornaam = voor_naam.get()
            tussenvoegsel= tussen_voegsel.get()
            achternaam = achter_naam.get()
            sqliteConnection = sqlite3.connect('SQlite_Phyton.db')
            print('Succesfully connected to SQlite')
            cursor = sqliteConnection.cursor()
            cursor.execute(f"select * from persoon where achternaam = '{achternaam}'")
            rows = cursor.fetchall()
            voor_naam.set(rows[0][1])
            tussen_voegsel.set(rows[0][2])
            achter_naam.set(rows [0][3])
            mo_biel.set(rows [0][4])
            cursor.close()
        except sqlite3.Error as error:
            print(f'Er ging iets mis :\n {error}')
        finally:
            if sqliteConnection:
                sqliteConnection.close()
            return "sqlite connection is closed"
    conn = sqlite3.connect("SQlite_Phyton.db")

Label(root, text= 'Zoek formulier', width=20, font=('bold',20)).place(x=90, y=53)

Label(root, text='Voornaam', width=20, font=('bold',10), anchor='w').place(x=68, y=130)
Entry(root, textvariable=voor_naam, width=30).place(x=200, y=132)

Label(root, text='Tussenvoegsel', width=20, font=('bold',10),anchor='w').place(x=68, y=160)
Entry(root, textvariable=tussen_voegsel, width=30).place(x=200, y=162)

Label(root, text='Achternaam', width=20, font=('bold',10), anchor='w').place(x=68, y=190)
Entry(root, textvariable=achter_naam, width=30).place(x=200, y=192)

Label(root, text='Mobiel', width=20, font=('bold',10), anchor='w').place(x=68, y=220)
Entry(root, textvariable=mo_biel, width=30).place(x=200, y=222)

Button(root, text='Submit', width=20, bg='pink', fg='black', command=database).place(x=200, y=250)

root.mainloop()