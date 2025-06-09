from tkinter import *
from tkinter import ttk, messagebox

GEO='250x150'
LIJST_ZICHTBAAR = 10

def items_selected(event):
    selected_indices = lbo_coureurs.curselection()
    selected_coureurs = ",".join([lbo_coureurs.get(i) for i in selected_indices])
    msg = f'You selected: {selected_coureurs}'
    messagebox.showinfo(title='Information', message=msg)


coureurs = ['Max Verstappen',
            'Daniel Ricciardo',
            'Lando Norris',
            'Sebastian Vettel',
            'Lewis Hamilton']

root = Tk()
root.geometry(GEO)
root.resizable(False, False)
root.title('Een Listbox with your favorite F1 drivers')
toplabel = Label(root, text="Kies u favoriete coureur")
toplabel.grid(column=0, row=0)
lbo_coureurs = Listbox(root, exportselection=0)

lbo_coureurs.bind('<<ListboxSelect>>', items_selected)

i = 0

for coureur in coureurs:
    lbo_coureurs.insert(i, coureur)
    i+= 1 

f1_cars = ('Renault', 'Ferrari', 'Honda', 'Mercedes')
string_f1_cars = StringVar(value=f1_cars)
lbo_f1_cars = Listbox(root, exportselection=0, listvariable=string_f1_cars,height=LIJST_ZICHTBAAR,selectmode='extended')

for indebox in dict(lbo_coureurs):
    print(indebox)

lbo_coureurs.grid(column=0,row=1)
lbo_f1_cars.grid(column=1, row=1, padx=20, pady=20)

root.mainloop()
