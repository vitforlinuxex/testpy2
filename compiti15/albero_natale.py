import shutil

def albero_natale(altezza=10, simbolo='*'):
    """
    Stampa un albero di Natale centrato nel terminale.

    :param altezza: Altezza dell'albero (numero di righe).
    :param simbolo: Simbolo utilizzato per disegnare l'albero.
    """
    # Prendi la larghezza del terminale
    larghezza = shutil.get_terminal_size().columns

    for i in range(altezza):
        # Numero di simboli per riga (numero dispari)
        n_simboli = 2 * i + 1
        # Costruisci la riga con i simboli
        riga = simbolo * n_simboli
        # Stampa centrando la riga
        print(riga.center(larghezza))

    # Stampa il tronco (altezza 2, larghezza 3 simboli)
    tronco_altezza = max(2, altezza // 4)
    tronco_larghezza = 3 if 3 <= larghezza else 1
    tronco = simbolo * tronco_larghezza
    for _ in range(tronco_altezza):
        print(tronco.center(larghezza))