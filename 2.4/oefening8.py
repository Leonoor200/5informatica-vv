voornaam = input("voornaam: ")
achternaam = input("achternaam: ")
functietitel = input("functietitel: ")

naam = f"{voornaam} {achternaam}".upper()

breedte = max(len(naam), len(functietitel)) + 4

rand = "+" + "-" * breedte + "+"
regel_naam = "|" + naam.center(breedte) + "|"
regel_functie = "|" + functietitel.center(breedte) + "|"

print(rand)
print(regel_naam)
print(regel_functie)
print(rand)