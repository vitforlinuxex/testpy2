def triangolo_equilatero(altezza):
    for i in range(1, altezza + 1):
        spazi = altezza - i
        asterischi = 2 * i - 1
        print(' ' * spazi + '*' * asterischi)

# Esempio di utilizzo
altezza = int(input("Inserisci l'altezza del triangolo equilatero: "))
triangolo_equilatero(altezza)