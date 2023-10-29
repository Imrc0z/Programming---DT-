#Rida Najibi

#Dit is een functie die als input je geboortejaar neemt en je leeftijd in Venus jaren retourneert. door middel van 3 getallen

def maximum_van_drie_getallen(a, b, c):
    return max(a, b, c)

def venus_jaar(geboortejaar):
    huidig_jaar = 2023  # Stel het huidige jaar in
    aards_leeftijd = huidig_jaar - geboortejaar
    venus_leeftijd = aards_leeftijd / 0.615
    return venus_leeftijd

# Test de maximum_van_drie_getallen functie met verschillende argumenten
getal1 = 5
getal2 = 10
getal3 = 3

max_resultaat = maximum_van_drie_getallen(getal1, getal2, getal3)
print(f"Het maximum van {getal1}, {getal2} en {getal3} is: {max_resultaat}")

# Test de venus_jaar functie met je eigen geboortejaar
geboortejaar = 1990  # Vervang dit door je eigen geboortejaar
venus_leeftijd = venus_jaar(geboortejaar)
print(f"Je leeftijd in Venus-jaren is ongeveer {venus_leeftijd:.2f} jaar.")