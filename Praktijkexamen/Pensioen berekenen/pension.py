# Functie voor het berekenen van het maand bedrag aan de hand van de leeftijd en werkstatuur

def week_bedrag (leeftijd, statuut):
    #Deze list bewaren de waardes die bij elkaar horen op de zelfde index positie en worden zo aan elkaar gekoppeld
    statuten=['medewerker','zelfstandige','ambtenaar']
    bedragen=[350, 300, 370]
    extra=[20, 15, 25]
    #Hier wordt er onderscheid gemaakt op de mensen ouder en jonger dan 70 jaar om de extra's te bepalen. Vervolgens word gekeken
    #wat hun werkstatuut is en welke index deze heeft in de list. Deze index word vervolgens gebruikt om het bijbehorende bedrag en extra te vinden.
    #Dit getal wordt dan terug gegeven.
    if leeftijd < 70:
        for i in statuten:
            if statuut == i:
                return bedragen[statuten.index(i)]
    else:
        for i in statuten:
            if statuut == i:
                return bedragen[statuten.index(i)] + extra[statuten.index(i)]

 #Hier wordt de gebruiker gevraagd om de leeftijd en werkstatuut in te voeren en deze worden opgelagen in de variabelen.
 # De leeftijd wordt ook nog omgezet naar een int om mee te kunnen rekenen.   
leeftijd = int(input("Wat is je leeftijd? \nVoer het aantal jaren in: "))
statuut = input("Wat is je werkstatuut? \nVoer in medewerker, zelfstandige of ambtenaar: ")

#Dit is de eerste check of de gebruiker wel oud genoeg is om pensioen gerechtigd is. Wanneer dit niet zo is wordt er vermeld hoeveel
#jaren ze nog moeten werken. Zijn ze wel gerechtigd dan wordt het bedrag berekend met de functie week_bedrag.
# Uiteindelijk wordt dan vermeld op hoeveel geld de gebruiker recht heeft elke week.
if leeftijd < 65:
    jaren = 65 - leeftijd 
    print(f"Van werken word je gelukkig, je mag nog {jaren} jaar genieten van je baan.")
else:
    bedrag = week_bedrag(leeftijd, statuut)
    print(f"Je krijgt {bedrag} per week.")
    

