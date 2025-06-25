from tkinter import *
from tkinter import ttk

# Hoofdscherm

root = Tk()
root.geometry('450x200')
root.resizable(False,False)
root.title('RGB colours')


# Variabelen voor huidige kleur waardes
current_red = DoubleVar()
current_blue = DoubleVar()
current_green = DoubleVar()

# Functies om huidige waardes van de sliders te bepalen. Deze worden opgehaald met de .get functie
#en omgezet naar een int die vervolgens wordt geformat naar een hexadecimaal getal waarbij de output minimaal twee getallen is
#daarna worden de hex waardes aanelkaar geplakt samen met # ervoor en als variable gebruikt om de achtergrond aan te passen
#ook worden hier de labels onder het canvas aangepast naar de waardes die op de sliders geselecteerd zijn.

def slider_change(event):
    rood = format(int(current_red.get()), '02x')
    blauw = format(int(current_blue.get()), '02x')
    groen = format(int(current_green.get()), '02x')
    kleur =f"#{rood}{groen}{blauw}"
   
    canvas.configure(bg=kleur)
    hex_value.configure(text= f'Hex code: {kleur}')
    rgb_value.configure(text=f'RGB: [{int(current_red.get())}, {int(current_green.get())}, {int(current_blue.get())}]')

#Title van de app

Label(root, text='RGB Colors').grid(column=0, row=0)

# Een canvas definieren om de kleur te laten zien.
canvas = Canvas(root,width=100, height=100, bg='black')
canvas.grid(column=0, row=3,sticky='s')

#Hier worden labels gemaakt om de RGB waardes te laten zien en de hexadecimaal code die gebruikt wordt om 
#de kleur aan het canvas te geven op basis van de sliders
rgb_value = Label(root, text="RGB: [00, 00, 00]")
rgb_value.grid(column=0, row=4)

hex_value = Label(root, text="Hex code: #000000")
hex_value.grid(column=0, row= 5)

#sliders definieren. Hier worden drie sliders aangemaakt voor de kleuren rood, groen en blauw
#Deze gaan allemaal van 0 tot 255 en zijn gelinkt aan de functie slider_change met een eigen variable.
slider_rood = Scale(root, label='Rood', from_=255, to=0, command=slider_change, variable=current_red)
slider_groen = Scale(root, label='Groen', from_=255, to=0, command=slider_change, variable=current_green)
slider_blauw = Scale(root, label='Blauw', from_=255, to=0, command=slider_change, variable=current_blue)


slider_rood.grid(column=1, row = 3, sticky='we')
slider_groen.grid(column=2, row = 3, sticky='we')
slider_blauw.grid(column=3, row = 3, sticky='we')


#Nog een button om de app af te sluiten
Button(root, text='Afsluiten', command=root.quit).grid(column=1, row=5, padx=10)

root.mainloop()
