gewicht = float(input("Wat is jouw gewicht in KG: "))
lengte = float(input("Geef je lengte in m: "))

print(gewicht)
print(lengte)

bmi = gewicht / (lengte * lengte)

print(f"Je BMI is {bmi:.1f}.")