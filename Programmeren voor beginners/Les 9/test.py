import math

def discriminant(a,b,c):
    # voor: ax^2 + bx + c
    D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    uitvoer=[D1, D2]
    return uitvoer

print("Voor de formule ax^2 + bx + c, geef a, b en c:")
a = -3 #int(input("Wat is a? "))
b = 2 #int(input("Wat is b? "))
c = 5 #int(input("Wat is c? "))

uitkomst = discriminant(a,b,c)

D1 = uitkomst[0]
D2 = uitkomst[1]

print(f"De discriminant(en) voor {a}x^2 + {b}x + {c} zijn:")
print(f"{D1} en {D2}")