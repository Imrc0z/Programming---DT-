#Opdracht 7

import random

#Kies een willekeurig getal tussen 0 en 5 en print het af.
willekeurig_getal = random.randint(0, 5)
print("Willekeurig gekozen getal tussen 0 en 5:", willekeurig_getal)

#Kies weer een willekeurig getal tussen 0 en 5, en vraag de gebruiker om een getal. Vergelijk de getallen en druk de juiste tekst af.

willekeurig_getal = random.randint(0, 5)
ingevoerd_getal = int(input("Raad het willekeurige getal tussen 0 en 5: "))

if willekeurig_getal == ingevoerd_getal:
    print("Goed geraden!")
else:
    print("Volgende keer beter.")