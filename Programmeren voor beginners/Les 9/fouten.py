import math

def discriminant(a,b,c):
    try:
        D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    except:
        D1 = "Geen oplossing"
        D2 = "Geen oplossing"

    uitvoer = [D1, D2]

    return uitvoer

print("Voor de formule ax^2 + bx + c, geef a, b en c:")

a = int(input("De waarde voor a is? "))
b = int(input("De waarde voor b is? "))
c = int(input("De waarde voor c is? "))

uitkomst = discriminant(a,b,c)

D1 = uitkomst[0]
D2 = uitkomst[1]

print(f"De discriminant(en) voor {a}x^2 + {b}x + {c} zijn: ")
print(f"{D1} en {D2}")