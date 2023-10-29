getallen = [3, 7, 0, 15]


print("Vermenigvuldigen met 2:")
for getal in getallen:
    resultaat = getal * 2
    print(resultaat, end=" ")


print("\Delen door 3 en afronden:")
for getal in getallen:
    resultaat = round(getal / 3, 1)
    print(resultaat, end=" ")