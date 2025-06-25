from tkinter import *
from tkinter import messagebox, ttk
import sqlite3

inlog = Tk()
inlog.title('Inloggen')

#functie om het inlog scherm te sluiten

def homepage():
    homepage = Toplevel(inlog)
    homepage.title('Homepage')

    voor_naam = StringVar()
    a_dres = StringVar()
    woon_plaats = StringVar()
    achternamen = ""

    def uitloggen():
        inlog.deiconify()
        homepage.destroy()

    def zoek():
        if cbo_achternamen.get() == "":
            messagebox.showerror('Error','Geen achternaam ingevuld')
            return FALSE
        else:    
            try:
                l_achternaam = cbo_achternamen.get()
                voornaam = voor_naam.get()
                adres = a_dres.get()
                woonplaats = woon_plaats.get()
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                cursor.execute(f"SELECT naam, adres, woonplaats FROM users CROSS JOIN naw WHERE achternaam = '{l_achternaam}'")
                data = cursor.fetchall()
                voor_naam.set(data[0][0])
                a_dres.set(data[0][1])
                woon_plaats.set(data[0][2])
                cursor.close()
            except sqlite3.Error as error:
                print(f"Er ging iets mis:\n {error}")
            finally:
                if conn:
                    conn.close()
   
    conn = sqlite3.connect('users.db')
    

    cbo_achternamen = ttk.Combobox(homepage, values=achternamen)

    Label(homepage, text='Homepage', width=20, font=('bold',20)).grid(column=0, row=0)

    Label(homepage, text='Achternaam', width= 20, font=('bold',10)).grid(column=0, row=1)
    cbo_achternamen.grid(column=1, row=1)

    Label(homepage, text='Voornaam:', width= 20, font=('bold',10)).grid(column=0, row=2)
    Entry(homepage, textvariable=voor_naam, width=30).grid(column=1, row=2)

    Label(homepage, text='Adres:', width= 20, font=('bold',10)).grid(column=0, row=3)
    Entry(homepage, textvariable=a_dres, width=30).grid(column=1, row=3)

    Label(homepage, text='Woonplaats:', width= 20, font=('bold',10)).grid(column=0, row=4)
    Entry(homepage, textvariable=woon_plaats, width=30).grid(column=1, row=4)

    Button(homepage, text='Zoek gegevens', width='30', command=zoek).grid(column=1, row=5)
    Button(homepage, text='Uitloggen', width='30', command=uitloggen).grid(column=2, row=5)

    inlog.withdraw()

def annuleren():
    inlog.destroy()

#functie om te kijken of de gebruiker een account heeft en het wachtwoord overeenkomt
def login():
    check = email.get()
    passw = password.get()

    conn = sqlite3.connect('users.db')
    with conn:
        
        cursor = conn.cursor()
        finduser = ("SELECT * FROM users WHERE email = ?")    
        cursor.execute(finduser,[(check)])
        row = cursor.fetchall()
        if row:
            if row[0][2] == passw:
                homepage()
            else:
                messagebox.showerror('Error','Password niet correct!')
        else:
            messagebox.showerror('Error','Gebruiker niet gevonden!')
        
    

#functie om een registaratie scherm te laten zien aan de gebruiker
def registreren():
    reg_window = Toplevel(inlog)
    reg_window.title('Registreren')
    
    #functie om de gebruiker in database te registreren.
    def insert_user():
        l_email = email1.get()
        l_password = password_reg.get()
    
        conn =sqlite3.connect('users.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)', (l_email, l_password))

        cursor.close()

    def insert_naw():
        l_naam = naam.get()
        l_achternaam = achternaam.get()
        l_adres = adres.get()
        l_woonplaats = woonplaats.get()
        l_email = email1.get()
        

        conn = sqlite3.connect('users.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM users WHERE email = '{l_email}'")
            rows = cursor.fetchall()
            cursor.execute('INSERT INTO naw(naam, achternaam, adres, woonplaats, idnaw) VALUES(?, ?, ?, ?, ?)', (l_naam, l_achternaam, l_adres, l_woonplaats, rows[0][0]))
            messagebox.showinfo('Geregistreerd', 'Succesvol geregistreerd')
        cursor.close()

    # functie om te controleren of de email adressen geldig zijn en overeenkomen voor het registeren van een nieuwe gebruiker
    def check():
        check1 = email1.get()
        check2 = email2.get()
        passw= password_reg.get()
       
    # Hier wordeen de twee email adressen met elkaar vergeleken en aan de gebruiker terug gekoppeld of de registratie geslaagd is of niet
        if check1 != check2:
            messagebox.showerror('Error', 'Email adres komt niet overeen')   
        else:
            try:
                conn = sqlite3.connect('users.db')
                create_users_querry="""CREATE TABLE IF NOT EXISTS users (
                                        iduser INTEGER PRIMARY KEY AUTOINCREMENT,
                                        email VARCHAR (45) NOT NULL,
                                        password VARCHAR (255) NOT NULL);"""
                create_NAW_querry ="""CREATE TABLE IF NOT EXISTS naw (
                                        idnaw INTEGER PRIMARY KEY,
                                        naam VARCHAR (45) NOT NULL,
                                        achternaam VARCHAR (45) NOT NULL,
                                        adres VARCHAR (255) NOT NULL,
                                        woonplaats VARCHAR (255) NOT NULL);"""
                with conn:
                    cursor = conn.cursor()
                    cursor.execute(create_users_querry)
                    cursor.execute(create_NAW_querry)
                    finduser = ("SELECT * FROM users WHERE email = ?")    
                    cursor.execute(finduser,[(check1)])
                    if cursor.fetchall():
                        print("Email adres al in gebruik")
                    else:
                        insert_user()
                        insert_naw()
                conn.commit()
            
            except sqlite3.Error as error:
                return f"Error while creating a SQLite database {error}"
            
            finally:
                if conn:
                    conn.close()
                    return"SQLite connection is closed"
        reg_window.destroy()
            

    def annuleren():
        reg_window.destroy()
    # functie om te kijken of er een bruikbaar email adres is ingevuld.
    def callback(i):
        check=""
        if i == 1:
            check = email1.get()
        if i == 2:
            check = email2.get()
        if check =="":
            messagebox.showerror('Error','Geen bruikbaar email adres ingevuld!')
            return False
        elif '@' and '.' not in check:
            messagebox.showerror('Error','Geen bruikbaar email adres ingevuld!')
            return False
        else:
            return True

# Dit zijn de variabelen die worden gevraad van de gebruiker om zich te registreren.    
    email1 = StringVar()
    email2 = StringVar()
    password_reg = StringVar()
    naam = StringVar()
    achternaam = StringVar()
    adres = StringVar()
    woonplaats = StringVar()

# Dit zijn  de Entry widgets en Labels die aan de gebruiker worde getoont.
    Label(reg_window, text='Email adres').grid(column=0, row=0)
    Entry(reg_window, textvariable=email1, validate='focusout', validatecommand= lambda: callback(1)).grid(column=1, row=0)

    Label(reg_window, text='Ter controle nogmaals email:').grid(column=0, row=1)
    Entry(reg_window, textvariable=email2, validate='focusout', validatecommand= lambda: callback(2)).grid(column=1, row=1)

    Label(reg_window, text='Password').grid(column=0, row=2)
    Entry(reg_window, show='*', textvariable=password_reg).grid(column=1, row=2)

    Label(reg_window, text='Voornaam:').grid(column=3, row=0)
    Entry(reg_window, textvariable=naam).grid(column=4, row=0)

    Label(reg_window, text='Achternaam:').grid(column=3, row=1)
    Entry(reg_window, textvariable=achternaam).grid(column=4, row=1)

    Label(reg_window, text='Adres:').grid(column=3, row=2)
    Entry(reg_window, textvariable=adres).grid(column=4, row=2)

    Label(reg_window, text='Woonplaats:').grid(column=3, row=3)
    Entry(reg_window, textvariable=woonplaats).grid(column=4, row=3)

    knop_reg2= Button(reg_window, text='Registreren', command = check).grid(column=0, row=4)
    knop_ann2= Button (reg_window, text='Annuleren', command = annuleren).grid(column=1, row=4)

#Dit zijn de variabelen die worden gevraagd aan de gebruiker om in te loggen

email=StringVar()
password=StringVar()

#De Entry widgets en labels die worden getoond op het inlog scherm.
Label(inlog, text='Email adres').grid(column=0, row=0)
Entry(inlog, textvariable=email).grid(column=1, row=0)

Label(inlog, text='Password').grid(column=0, row=1)
Entry(inlog, show='*', textvariable=password).grid(column=1, row=1)

knop_reg= Button(inlog, text='Registreren', command = registreren).grid(column=0, row=2)
knop_ann= Button (inlog, text='Annuleren', command= annuleren).grid(column=1, row=2)
knop_log= Button (inlog, text='Login', command = login).grid(column=2, row=2)

inlog.mainloop()



