# ------------  SVILUPPATORE 3) --------------


"""
def verifica_user(user):
    return True
def verifica_password(password):
    return True
"""

"""
vorrei fare una funzione in python che invii i dati di una variabile in un file .txt nella cartella dell utente corrente
"""
from pathlib import Path

def scrivi_su_file_nella_home(nome_file, dati):
    home_dir = Path.home()
    percorso_file = home_dir / nome_file
    
    with percorso_file.open('w', encoding='utf-8') as file:
        file.write(str(dati))
    
    print(f"Dati scritti in: {percorso_file}")

"""
crea una funzione in python che controlli se un nome utente nella forma di un indirizzo email non è nalla lista contenuta nella funzione con 10 indirizzi email di fantasia e se nell indirizzo email sono contenuti una chiocciola e un punto
"""
def verifica_user(user):
    # Lista di 10 indirizzi email di fantasia
    lista_email = [
        "alice@example.com",
        "bob.smith@mail.com",
        "charlie123@server.net",
        "daniella_99@domain.org",
        "franco.bianchi@xyz.it",
        "grazia.rossi@abc.com",
        "marco_totti@mail.net",
        "luca.verdi123@web.org",
        "elena.ferrari@company.com",
        "paolo_neri@mail.it"
    ]
    
    email_lower = user.lower()
    
    # Controlla presenza in lista (case insensitive)
    if email_lower in (e.lower() for e in lista_email):
        print("nome utente non valido\n")
        return False
    
    # Controlla presenza di almeno una chiocciola e un punto
    if '@' not in user or '.' not in user:
        print("assicurarsi della corretta forma dell\'indirizzo email\n")
        return False
    
    return True


"""

#crea una funzione in python per il controllo di una stringa, deve contenere almeno 8 caratteri, numeri e lettere, almeno una Maiuscola, almeno un carattere speciale a scelta tra ".,-_#!?%&$", non  deve contenere",/,\,(),{},[]"

"""
# import verifica_requisiti
import re

def verifica_password(password):
    # Controlla lunghezza minima
    if len(password) < 8:
        return False
    
    # Controlla almeno una lettera maiuscola
    if not re.search(r'[A-Z]', password):
        return False
    
    # Controlla almeno un numero
    if not re.search(r'[0-9]', password):
        return False
    
    # Controlla almeno un carattere speciale tra quelli consentiti
    if not re.search(r'[.,\-_#!?%&$]', password):
        return False
    
    # Controlla che non ci siano caratteri proibiti: ", /, \, (, ), {, }, [
    if re.search(r'["/\\()[\]{}]', password):
        return False
    
    # Se sono passati tutti i controlli
    return True


print("Benvenuto nella pagina di iscrizione al nostro sito.\nPer registrarti dovrai scegliere uno username inserendo la tua email e una password che rispetti i seguenti requisiti:")
print("\t\tAlmeno 8 caratteri\n\t\tSia numeri che lettere\n\t\tAlmeno una Maiuscola\n\t\tAlmeno un carattere speciale a scelta tra .,-_#!?%&$\n\t\tNon sono consentiti i seguenti caratteri: \", /,\,(),{},[]")
"""
# per fini didattici la verifica sullo user la facciamo con un ciclo while, mentre la verifica sulla password
# la facciamo simulando un do-while
#
"""
while True:
    user = input("Scegli il nome utente: \n\t")
    if verifica_user(user): break
    else: print("Attenzione, inserire una email valida!")

password = input("Scegli la tua password: \n\t")
while not verifica_password(password):
    print("Attenzione, la password non rispetta i requisiti richiesti. Sceglierne una nuova.") 
    password = input("Scegli la tua password \n\t")

print("User e password rispettano i requisiti.\nTi verrà inviata una email con il riepilogo dei dati di login. \nOra verrai reindirizzato alla schermata di login.")
print(f"\n\n*-------------------------*\nDati di Login:\n\t\tUsername:\t{user}\n\t\tPassword:\t{password}\n*-------------------------*")
variabile = f"\n\n*-------------------------*\nDati di Login:\n\t\tUsername:\t{user}\n\t\tPassword:\t{password}\n*-------------------------*"
scrivi_su_file_nella_home("user_pass_output.txt", variabile)
#------------SVILUPPATORE 4)-------------

# Ripasso sintassi ciclo while:
# while condizione True:
#   espressioni o istruzioni
