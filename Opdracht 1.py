# Gegeven lijst
steden = ["Amsterdam", "Praag", "Lissabon", "Londen", "Parijs", "Milaan"]

# 1. Druk achtereenvolgens af: het eerste, derde en laatste element.
print(steden[0])      # Eerste element
print(steden[2])      # Derde element
print(steden[-1])     # Laatste element

# 2. Bepaal het aantal elementen in de lijst met steden.
aantal_elementen = len(steden)
print(aantal_elementen)  # Dit zal 6 afdrukken

# 3. Bepaal het aantal letters in de tweede string ("Praag").
aantal_letters_in_praag = len(steden[1])
print(aantal_letters_in_praag)  # Dit zal 5 afdrukken

# 4. Voeg items toe aan de lijst met behulp van de += operator.
steden += ["Brussel", "Warschau"]
print(steden)  # Dit zal de uitgebreide lijst afdrukken

# 5. Pas het eerste element aan van "Amsterdam" naar "Rotterdam".
steden[0] = "Rotterdam"

# 6. Controleer het resultaat door de lijst met steden opnieuw af te drukken.
print(steden)  # Dit zal de bijgewerkte lijst met "Rotterdam" afdrukken
