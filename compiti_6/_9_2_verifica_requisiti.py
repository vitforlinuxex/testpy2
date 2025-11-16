# Creiamo il modulo esterno che conterrà le funzioni ausiliarie
# per il nostro programma.
# I moduli esterni sono quindi degli oggetti particolari appartenenti
# alla classe module.
# Servono per contenere e richiamare principalmente altre 3 tipologie
# di oggetti: funzioni, classi, costanti.
# E' sufficiente creare il file e salvarlo come .py

# Dopodiché, una volta importato, per poter utilizzare gli oggetti contenuti
# al suo interno, occorre richiamarli al solito modo: con il punto.
# Poiché sono esattamente come metodi ed attributi di un normalissimo
# oggetto. Ricordiamo che le funzioni nella pancia di un oggetto si chiamano
# metodi, e le cose dentro la pancia degli oggetti si richiama col punto.

# ------------  SVILUPPATORE 5) --------------

# ------------  SVILUPPATORE 1) --------------

def verifica_user(user):
    if "@" in user and "." in user:
        return True
    else:
        return False

# ------------  SVILUPPATORE 2) --------------
def verifica_password(password):
    check_lunghezza = 0
    if len(password) >= 8: check_lunghezza = 1
    check_numeri = 0
    for n in password:
        if n in "0123456789":
            check_numeri = 1
            break
    check_lettere = 0
    for n in password:
        if n.lower() in "abcdefghijklmnopqrstuvwxyz":
            check_lettere = 1
            break
    check_maiuscole = 0
    for n in password:
        if n in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            check_maiuscole = 1
            break
    check_speciali = 0
    for n in password:
        if n in ".,-_#!?%&$":
            check_speciali = 1
            break
    check_proibiti = 1    
    for n in password:
        if n in "\\/\\,\\(\\)\\{\\}\\[\\]":
            check_proibiti = 0
            break
    risultato = check_lunghezza*check_numeri*check_lettere*check_maiuscole*check_speciali*check_proibiti
    if risultato == 1: return True
    elif risultato == 0: return False
        
        
   
                
    
    
    
    
    
    
    