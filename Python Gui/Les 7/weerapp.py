from tkinter import *
from tkinter import messagebox
import requests

#constanten
TITLE = 'Weather Service'
WIDTH = 800
HEIGHT = 600

#Api-sleutel voor toegang weerdienst
API_KEY ='1edf0c2f560fb2d523c8ef4000b723d2'
#URL voor de weer-API met placeholders voor de locatie en API-sleutel
URL ='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

#Hoofdfunctie om het GUI-venster te starten
def start():
    #Maak de variabelen globaal zodat ze in andere functies beschikbaar zijn
    global root, city_name, state_code, country_code, keuze

    #Maak het hoofdvenster van de GUI en stel de titel in
    root = Tk()
    root.title(TITLE)
    #Stel de afmetingen van het venster input
    root.geometry(f'{WIDTH}x{HEIGHT}')

    #Maak en plaats het label en invoerveld voor de API-sleutel
    create_label(root, 'API_KEY:', 10, 10)
    api_key_var = StringVar(value=API_KEY)
    Entry(root, textvariable=api_key_var, width=60).place(x=120, y=10)

    #Maak en plaats het label en invoerveld voor de naam van de stad of dorp
    create_label(root, 'Naam stad/dorp: ', 10, 40)
    city_name = StringVar()
    Entry(root, textvariable=city_name, width= 60).place(x=120, y=40)

    #Maak en plaats het label en invoerveld voor de provincie/staat code
    create_label(root, 'Provincie/Staat code: ', 10, 70)
    state_code = StringVar()
    Entry(root, textvariable=state_code, width=60).place(x=120, y=70)

    #Maak en plaats het label en invoerveld voor de landcode
    create_label(root, 'Landcode', 10, 100)
    country_code = StringVar()
    Entry(root, textvariable=country_code, width=60).place(x=120, y=100)

    #Maak en plaats de knop om de weerdienst aan te roepen
    create_button(root, 'Roep weerdienst aan', 10, 130)

    #Maak en plaats de radioknoppen voor de verschillende zoekopties
    create_radio_button(root, 10, 160)

    #Maak een leeg label voor foutmeldingen of resultaten
    create_label(root, '', 10, 200)

    root.mainloop()

# Functie om radioknoppen te maken voor de zoekopties
def create_radio_button(frame, x_pos, y_pos):
    global keuze
    # Stel de standaardkeuze in voor de radioknoppen
    keuze = IntVar(value=1)

    #Maak en plaats de radioknoppen voor de verschillende zoekopties
    Radiobutton(frame, text='Naam stad/dorp', variable=keuze, value=1).place(x=x_pos, y=y_pos)
    Radiobutton(frame, text='Staat/Provincie + Stad', variable=keuze, value=2).place(x=x_pos, y=y_pos + 20)
    Radiobutton(frame, text='Land + Staat + Stad', variable=keuze, value=3).place(x=x_pos, y=y_pos + 40)
    
#Functie om een knop te maken en te plaatsen:
def create_button(frame,text, x_pos, y_pos):
    Button(frame, text=text, command= call_weather_service).place(x=x_pos, y= y_pos)

#Functie om een label te maken en te plaatsen
def create_label(frame, text, x_pos, y_pos):
    Label(frame, text=text).place(x=x_pos, y=y_pos)

#Functie om de weerdienst aan te roepen en de resultaten weer te geven
def call_weather_service():
    global city_name, state_code, country_code, keuze

    zoek =''

    try:
        #Bepaal de zoekoptie op basis van de selectie van de gebruiker
        if keuze.get() == 1:
            zoek = city_name.get()
        elif keuze.get() == 2:
            zoek = f"{city_name.get()},{state_code.get()}"
        elif keuze.get() == 3:
            zoek = f"{city_name.get()},{state_code.get()},{country_code.get()}"
    except Exception as e:
        #Toon een foutmelding als er iets misgaat bij het bepalen van de zoekoptie
        messagebox.showerror('Foutmelding', str(e))
        return
    
    try:
        #Maak de API-aanroep met de opgegeven zoekterm en API-sleutel
        response = requests.get(URL.format(zoek,API_KEY))
        weather_data = response.json()

        #Controleer of de API-aanroep succesvol was en of er een zoekterm is opgegeven
        if response.status_code != 200 or not zoek:
            create_label(root, 'Geen weerdata beschikbaar', 10, 250)
        else:
            #Maak een Listbox om de weerinformatie te tonen
            l_weather = Listbox(root, width=90, height=14)
            l_weather.place(x=10, y=250)

            #Haal de temperatuur in Kelvin op
            temp_kelvin = weather_data['main']['temp']
            # Zet de temperatuur om naar Celsius
            temp_celsius = temp_kelvin - 273.15

            #Toon de temperatuur in Celsius in de Listbox
            l_weather.insert(END, f"Temperatuur: {temp_celsius:.2f} Celius")

            #Voeg andere weerinformatie toe (behalve 'main' omdat de temperatuur al is verwerkt)
            for key, value in weather_data.items():
                if key != 'main':
                    l_weather.insert(END, f'{key} = {value}')
    
    except Exception as e:
        #Toon een foutmelding als er iets misgaat bij de API-aanroep
        messagebox.showerror('Foutmelding', str(e))

# De main-aanroep, het startpunt van het programma
if __name__ == '__main__':
    #Debug-melding om aan te geven dat de applicatie is gestart
    print('Applicatie gestart')
    #Start de GUI door de start-functie aan te roepen
    start()
    
    