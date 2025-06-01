achternaam=[]

def inlezen(bestand):
    global achternaam
    regels=[]

    with open(bestand) as f:
        regels.append(f.readlines())

    for regel in regels:
        print(regel)

        for persoonsgegevens in regel:
            achternaam.append(persoonsgegevens.split(',')[0])
            print(achternaam)
    
    return achternaam
    