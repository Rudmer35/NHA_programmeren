def vergelijking (getal1, getal2):
    if getal1 == getal2:
        print("De getallen zijn gelijk aan elkaar")

        return True
    else:
        print("De getallen zijn niet gelijk aan elkaar")

        return False
    
print("Geef twee getallen om te kijken of ze gelijk aan elkaar zijn")
getal1 = input("Geef waarde voor getal 1: ")
getal2 = input ("Geef waarde voor getal 2: ")

antwoord = vergelijking(getal1, getal2)
print(antwoord)