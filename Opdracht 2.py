while True:
    tafel = int(input("Welke tafel wilt u printen (0 = stoppen)? "))

    if tafel == 0:
        break  # Stop het programma als de gebruiker 0 kiest

    aantal_getallen = int(input("Hoeveel getallen wilt u printen? "))

    print(f"De tafel van {tafel}:", end=" ")

    for i in range(1, aantal_getallen + 1):
        resultaat = tafel * i
        print(resultaat, end=" ")

    print()  # Print een lege regel om de uitvoer te scheiden
