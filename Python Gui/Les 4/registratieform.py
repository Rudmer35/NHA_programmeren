from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x300')
root.title('Registratie formulier')

voornaam = StringVar()
tussenvoegsel = StringVar()
achternaam = StringVar()
mobiel = StringVar()

def database():
    l_voornaam = voornaam.get()
    l_tussenvoegsel = tussenvoegsel.get()
    l_achternaam = achternaam.get()
    l_mobiel = mobiel.get()

    conn = sqlite3.connect("SQlite_Phyton.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute('insert into persoon(voornaam, tussenvoegsel, achternaam, mobiel) values (?, ?, ?, ?)', (l_voornaam, l_tussenvoegsel, l_achternaam, l_mobiel))
    
    conn.commit()

req_label = Label(root, text= 'Registratie formulier', width=20, font=('bold',20))
req_label.place(x=90, y=53)

Label(root, text='Voornaam', width=20, font=('bold',10), anchor='w').place(x=68, y=130)
Entry(root, textvariable=voornaam, width=30).place(x=200, y=132)

Label(root, text='Tussenvoegsel', width=20, font=('bold',10),anchor='w').place(x=68, y=160)
Entry(root, textvariable=tussenvoegsel, width=30).place(x=200, y=162)

Label(root, text='Achternaam', width=20, font=('bold',10), anchor='w').place(x=68, y=190)
Entry(root, textvariable=achternaam, width=30).place(x=200, y=192)

Label(root, text='Mobiel', width=20, font=('bold',10), anchor='w').place(x=68, y=220)
Entry(root, textvariable=mobiel, width=30).place(x=200, y=222)

Button(root, text='Sla op in DB', width=20, bg='pink', fg='black', command=database).place(x=200, y=250)

root.mainloop()