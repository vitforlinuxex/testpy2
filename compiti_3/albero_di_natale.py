def albero_natale(altezza):
    for i in range(altezza):
        # Spazi per centrare gli asterischi
        print(' ' * (altezza - i - 1) + '*' * (2 * i + 1))
    # Tronco dell'albero
    for j in range(altezza // 3):
        print(' ' * (altezza - 1) + '*')

# Esempio di utilizzo
altezza_albero = 7
albero_natale(altezza_albero)