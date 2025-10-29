def triangolo_asterischi(altezza):
    for i in range(1, altezza + 1):
        print('*' * i)

# Esempio di utilizzo
altezza = int(input("Inserisci l'altezza del triangolo: "))
triangolo_asterischi(altezza)