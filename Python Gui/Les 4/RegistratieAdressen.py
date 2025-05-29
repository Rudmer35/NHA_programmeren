import sqlite3
from tkinter import *

#aanmaken van de root Tkinter pagina
root = Tk()
root.title('Adressen registratie')

#Variablen definieren voor de Entry fields
naam = StringVar()
adres = StringVar()

#Functie aanmaken voor het maken/connectie leggen met een database en hier de gegevens uit de Entryfields in op te slaan
def database():
    l_naam = naam.get()
    l_adres = adres.get()
    try:
        conn = sqlite3.connect('adressen.db')
        create_adres_querry= """CREATE TABLE IF NOT EXISTS adressen (
        idpersoon INTEGER PRIMARY KEY AUTOINCREMENT,
        naam VARCHAR (45) NOT NULL,
        adres VARCHAR(255) NOT NULL);"""
        with conn:
            cursor= conn.cursor()
            print("Succesfully connected to sqlite")
            cursor.execute(create_adres_querry)
            cursor.execute('INSERT INTO adressen(naam, adres) VALUES(?, ?)', (l_naam, l_adres))
        conn.commit()

    except sqlite3.Error as error:
        return f"Error while creating a sqlite tabel {error}"
    
    finally:
        if conn:
            conn.close()
            return "SQlite connection is closed"

#De Entry fields voor het formulier met bij behorende labels en een Submit button

Label(root, text= 'Registratie formulier', width=20, font=('bold',20)).place(x=90, y=53)

Label(root, text='Naam', width=20, font=('bold',10), anchor='w').place(x=68, y=130)
Entry(root, textvariable= naam, width=30).place(x=200, y=132)

Label(root, text='adres', width=20, font=('bold',10),anchor='w').place(x=68, y=160)
Entry(root, textvariable= adres, width=30).place(x=200, y=162)

Button(root, text='Submit', width=20, bg='pink', fg='black', command=database).place(x=200, y=250)

root.mainloop()