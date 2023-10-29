# Valutawisselkoersen
wisselkoersen = {
    1: 0.88,  # US dollar naar euro
    2: 1.17,  # GB pounds naar euro
    3: 0.009,  # Yen naar euro
}

# Vraag de gebruiker om valuta en bedrag
valuta_keuze = int(input("Valuta (1 = US dollar, 2 = GB pounds, 3 = Yen): "))
in_te_wisselen_bedrag = float(input("In te wisselen bedrag: "))

# Bereken de omgerekende waarde
if valuta_keuze in wisselkoersen:
    wisselkoers = wisselkoersen[valuta_keuze]
    omgerekend_bedrag = in_te_wisselen_bedrag * wisselkoers

    # Bereken transactiekosten
    transactiekosten = min(max(omgerekend_bedrag * 0.015, 2.0), 15.0)

    # Totaalbedrag
    totaal_bedrag = omgerekend_bedrag - transactiekosten

    # Print de resultaten
    print(f"Voor {in_te_wisselen_bedrag} {valuta_keuze} krijgt u {round(omgerekend_bedrag, 2)} Euro.")
    print(f"De transactiekosten bedragen {round(transactiekosten, 2)} Euro. U ontvangt {round(totaal_bedrag, 2)} Euro.")
else:
    print("Ongeldige valutakeuze. Voer 1, 2 of 3 in voor respectievelijk US dollar, GB pounds en Yen.")