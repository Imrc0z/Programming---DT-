#Opdracht 4

    score = int(input("Voer een score in (0-100): "))

    # Controleer of de score ongeldig is (buiten het bereik 0-100)
    if score < 0 or score > 100:
        print("Ongeldige score")
    # Controleer of de score geweldig is (80 of hoger)
    elif score >= 80:
        print("Geweldig")
    # Controleer of de score voldoende is (55 of hoger maar lager dan 80)
    elif score >= 55:
        print("Voldoende")
    # Als geen van de bovenstaande voorwaarden waar is, is de score onvoldoende
    else:
        print("Onvoldoende")