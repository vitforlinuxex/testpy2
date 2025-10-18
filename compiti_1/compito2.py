# Definiamo la funzione per il conteggio delle parole per risolvere il primo step del problema
def conta_parole(testo):
    # Separo le parole tramite lo spazio dato che non indico nessun carattere dentro la funzione split
    parole = testo.split()

    # Restituisco il numero di parole grazie alla parola chiave `return`, 
    # seguita dalla funzione len() che restituisce la lunghezza dell'oggetto passato come parametro
    return len(parole)

# Ora definiamo la funzione per contare le vocali, le consonanti, i spazi e i caratteri speciali
def analizza_stringa(testo):
    # Inizializzo i contatori per le variabili richieste
    num_vocali = 0
    num_consonanti = 0
    num_spazi = 0
    num_numeri = 0
    num_car_spec = 0

    # Definisco una lista di vocali
    vocali_lista = ['a', 'e', 'i', 'o', 'u', 'è', 'y', 'j']

    # Analizzo ogni carattere nella stringa di input
    for carattere in testo:
        # Verifico se il carattere è una vocale convertendola in minuscolo grazie al metodo lower() 
        # altrimenti se fosse maiuscola non soddisferebbe questa condizione e proseguirebbe oltre
        if carattere.lower() in vocali_lista:
            num_vocali += 1
        # Verifico se il carattere è una consonante grazie al metodo isalpha()
        elif carattere.isalpha():
            num_consonanti += 1
        # Verifico se il carattere è uno spazio grazie al metodo isspace()p
        elif carattere.isspace():
            num_spazi += 1
        # Verifico se il carattere è un numero grazie al metodo isnumeric()
        elif carattere.isnumeric():
            num_numeri += 1
        # Se le condizioni precedenti non sono soddisfatte significa che il resto saranno caratteri speciali, quindi li conto
        else:
            num_car_spec += 1

    # Restituisco i risultati
    return num_vocali, num_consonanti, num_spazi, num_numeri, num_car_spec

  
nome = input("come ti chiami?\n ")
# Esempio di utilizzo della funzione conta_parole()
num_parole = conta_parole(nome)
print("Numero di parole nel testo:", num_parole)
  
  
# Esempio di utilizzo della funzione analizza_stringa()
num_vocali, num_consonanti, num_spazi, num_numeri, num_car_spec = analizza_stringa(nome)
print("Vocali:", num_vocali)
print("Consonanti:", num_consonanti)
print("Spazi:", num_spazi)
print("Numeri:", num_numeri)
print("Altri caratteri:", num_car_spec)