from tkinter import *
from tkinter import ttk
from file_utils import inlezen

name =''

def inlezen_bestand():
    global namen
    string =['']
    cbo_coureurs.delete(0, END)
    namen = inlezen('coureurs_namen.txt')
    i = len (cbo_coureurs['values'])
    for naam in namen:
        coureurs.append(naam)
    
    cbo_coureurs['values'] = coureurs
    cbo_coureurs.current(1)

def change_coureurs():

    cbo_coureurs['values'] =['Niki Lauda'
                            ,'Mario Andretti'
                            ,'Emerson Fittipaldi'
                            ,'Juan Manuel Fangio'
                            ,'Jos Verstappen']
    

geo = '250x100'

coureurs = ['Max Verstappen',
            'Daniel Ricciardo',
            'Lando Norris',
            'Sebastian Vettel',
            'Lewis Hamilton']

root = Tk()
root.geometry(geo)
root.title('Een combobox met je favoriete F1 coureurs')
toplabel = Label(root, text= 'Kies u favoriete coureur')
toplabel.grid(column=0, row=0)
cbo_coureurs = ttk.Combobox(root, values= coureurs)

for indebox in dict(cbo_coureurs):
    print(indebox)

cbo_coureurs.grid(column=0, row=1)

add_namen_button = Button(root, text='Voeg namen toe', command= inlezen_bestand)
add_namen_button.grid(column=0, row=3)

cbo_coureurs.current(4)
print(cbo_coureurs.current())
print(cbo_coureurs.get())

str_coureur = StringVar()
str_coureur = cbo_coureurs.get()

coureurlabel = Label(root, text=cbo_coureurs.get())
coureurlabel.grid(column=0, row=2)
print(f'de waarde van {str_coureur}')

root.mainloop()