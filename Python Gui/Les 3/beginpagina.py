from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Inloggen')

# funtie om het inlog scherm te sluiten

def annuleren():
    root.destroy()

#functie om te kijken of de gebruiker een account heeft en de het wachtwoord overeenkomt
def login():
    check = email.get()
    passw = password.get()

    if check in users:
        if users[check] == passw:
            homepage = Tk()
            homepage.title('Homepage')
            root.destroy()
        else:
            messagebox.showerror('Error','Password niet correct')
    else:
        messagebox.showerror('Error', 'Gebruiker niet gevonden')
#functie om een registaratie scherm te laten zien aan de gebruiker
def registreren():
    reg_window = Toplevel(root)
    reg_window.title('Registreren')
    # functie om te controleren of de email adressen geldig zijn en overeenkomen voor het registeren van een nieuwe gebruiker
    def check():
        check1 = email1.get()
        check2 = email2.get()
        passw= password_reg.get()
# Hier wordeen de twee email adressen met elkaar vergeleken en aan de gebruiker terug gekoppeld of de registratie geslaagd is of niet
        if check1 != check2:
            messagebox.showerror('Error', 'Email adres komt niet overeen')   
        elif check1 in users:
                messagebox.showerror('Error', 'Email adres al in gebruik')
        else:
            users[check1] = passw
            messagebox.showinfo('Geregistreerd', 'Succesvol geregistreerd')
            reg_window.destroy()
        
# Deze functie wordt gebruikt om het registratie window te sluiten
    def annuleren():
        reg_window.destroy()
# Deze functie wordt gebruikt om te kijken of er een bruikbaar email adres is ingevuld.
    def callback(i):
        check =""
        if i == 1:
            check = email1.get()
        if i == 2:
            check = email2.get()
        if check =="":
            messagebox.showerror('Error', 'Geen email adres ingevuld')
            return False
        elif '@' and '.' not in check:
            messagebox.showerror('Error','Geen bruikbaar email adres')
            return False
        else:
            return True
        
              
# Dit zijn de variabelen die worden gevraad van de gebruiker om zich te registreren.    
    email1 = StringVar()
    email2 = StringVar()
    password_reg = StringVar()
# Dit zijn  de Entry widgets en Labels die aan de gebruiker worde getoont.
    Label(reg_window, text='Email adres').grid(column=0, row=0)
    Entry(reg_window, textvariable=email1, validate='focusout', validatecommand= lambda: callback(1)).grid(column=1, row=0)

    Label(reg_window, text='Ter controle nogmaals email:').grid(column=0, row=1)
    Entry(reg_window, textvariable=email2, validate='focusout', validatecommand= lambda: callback(2)).grid(column=1, row=1)

    Label(reg_window, text='Password').grid(column=0, row=2)
    Entry(reg_window, show='*', textvariable=password_reg).grid(column=1, row=2)

    knop_reg2= Button(reg_window, text='Registreren', command = check).grid(column=0, row=3)
    knop_ann2= Button (reg_window, text='Annuleren', command = annuleren).grid(column=1, row=3)

#Dit zijn de variabelen die worden gevraagd aan de gebruiker om in te loggen

email=StringVar()
password=StringVar()

#Een dict. om de gerbuikers die zich hebben geregistreed op te slaan.
users ={}

#De Entry widgets en labels die worden getoond op het inlog scherm.
Label(root, text='Email adres').grid(column=0, row=0)
Entry(root, textvariable=email).grid(column=1, row=0)

Label(root, text='Password').grid(column=0, row=1)
Entry(root, show='*', textvariable=password).grid(column=1, row=1)

knop_reg= Button(root, text='Registreren', command = registreren).grid(column=0, row=2)
knop_ann= Button (root, text='Annuleren', command= annuleren).grid(column=1, row=2)
knop_log= Button (root, text='Login', command = login).grid(column=2, row=2)

root.mainloop()

