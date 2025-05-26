from tkinter import *
from tkinter import messagebox

root = Tk()
root.title='Rekenmachine'

getal1=''
getal2=''

rekenteken_gekozen = False
rekenteken = ''

Uitvoer = StringVar()
Uitvoer.set('Antwoord') 

def reken(a):
    global rekenteken_gekozen
    global rekenteken
    global getal1
    global getal2

    if getal2 != '':
        #uitrekenen
        pass
    
    rekenteken = a
    rekenteken_gekozen = True
    Uitvoer.set(getal1 + rekenteken)

def invoer(a):
    global getal1
    global getal2
    global rekenteken_gekozen
    global rekenteken

    if not rekenteken_gekozen:
        getal1 += a
        Uitvoer.set(getal1)
    else:
        getal2 += a
        Uitvoer.set(getal1 + rekenteken + getal2)

def uitrekenen():
    global getal1
    global getal2
    global rekenteken_gekozen

    getal1_float = float(getal1)
    getal2_float = float(getal2)

    if rekenteken == '+':
        antwoord = getal1_float + getal2_float
        Uitvoer.set(antwoord)
    elif rekenteken == '-':
        antwoord = getal1_float - getal2_float
        Uitvoer.set(antwoord)
    elif rekenteken == '*':
        antwoord = getal1_float * getal2_float
        Uitvoer.set(antwoord)
    elif rekenteken == '/':
        antwoord = getal1_float / getal2_float
        Uitvoer.set(antwoord)
    getal1 = str(antwoord)
    getal2 = ''
    rekenteken_gekozen = False  

def clear():
    global getal1
    global getal2
    global rekenteken
    global rekenteken_gekozen
    global Uitvoer

    rekenteken_gekozen = False
    rekenteken = ''
    getal1 =''
    getal2 =''
    Uitvoer.set('')  


# Knoppen definieeren
knop_zeven = Button(root, text='7', width=2, height=2, command=lambda: invoer('7'))
knop_acht = Button(root, text='8', width=2, height=2, command=lambda: invoer('8'))
knop_negen = Button(root, text='9', width=2, height=2, command=lambda: invoer('9'))
knop_delen = Button(root, text='/', width=2, height=2, command=lambda: reken('/'))
knop_vier = Button(root, text='4', width=2, height=2, command=lambda: invoer('4'))
knop_vijf = Button(root, text='5', width=2, height=2, command=lambda: invoer('5'))
knop_zes = Button(root, text='6', width=2, height=2, command=lambda: invoer('6'))
knop_keer = Button(root, text='*', width=2, height=2, command=lambda: reken('*'))
knop_een = Button(root, text='1', width=2, height=2, command=lambda: invoer('1'))
knop_twee = Button(root, text='2', width=2, height=2, command=lambda: invoer('2'))
knop_drie = Button(root, text='3', width=2, height=2, command=lambda: invoer('3'))
knop_min = Button(root, text='-', width=2, height=2, command=lambda: reken('-'))
knop_nul = Button(root, text='0', width=2, height=2, command=lambda: invoer('0'))
knop_punt = Button(root, text='.', width=2, height=2, command=lambda: invoer('.'))
knop_plus = Button(root, text='=', width=2, height=2, command=uitrekenen)
knop_gelijk = Button(root, text='+', width=2, height=2, command=lambda: reken('+'))
label_Uitvoer = Label(root, textvariable=Uitvoer, width = 8, height=2, bg='black', fg='white')
knop_CE = Button(root, text='CE', width=2, height=2, command=clear)

#Layout knoppen grid

knop_zeven.grid(row=0, column=0)
knop_acht.grid(row=0, column=1)
knop_negen.grid(row=0, column=2)
knop_delen.grid(row=0, column=3)
knop_vier.grid(row=1, column=0)
knop_vijf.grid(row=1, column=1)
knop_zes.grid(row=1, column=2)
knop_keer.grid(row=1, column=3)
knop_een.grid(row=2, column=0)
knop_twee.grid(row=2, column=1)
knop_drie.grid(row=2, column=2)
knop_min.grid(row=2, column=3)
knop_nul.grid(row=3, column=0)
knop_punt.grid(row=3, column=1)
knop_plus.grid(row=3, column=2)
knop_gelijk.grid(row=3, column=3)
label_Uitvoer.grid(row=4, column=0, columnspan=3, sticky='nesw')
knop_CE.grid(row=4, column=3)


root.mainloop()