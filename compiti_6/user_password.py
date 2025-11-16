import json
import os
"""
ho bisogno di una funzione in python che scriva nome utente in forma di indirizzo e-mail e password in chiaro per motivi didattici su un file user_password in json e di un altra funzione che controlli se l'utente esiste e la password per il login
"""

FILE_PATH = "user_password.json"
EMAIL_DOMAIN = "example.com"

def save_user_password(username, password):
    """
    Salva l'utente e la password in chiaro nel file JSON.
    L'username viene convertito in indirizzo email.
    """
    email = f"{username}@{EMAIL_DOMAIN}"
    
    # Carica i dati esistenti
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
    else:
        data = {}
    
    # Aggiungi o aggiorna l'utente
    data[email] = password
    
    # Salva i dati sul file
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Utente {email} salvato con password in chiaro (attenzione: solo didattico).")

def check_login(username, password):
    """
    Verifica se l'utente esiste e se la password è corretta.
    Ritorna True se login valido, False altrimenti.
    """
    email = f"{username}@{EMAIL_DOMAIN}"
    
    if not os.path.exists(FILE_PATH):
        print("Nessun utente registrato.")
        return False
    
    with open(FILE_PATH, "r") as f:
        data = json.load(f)
    
    if email not in data:
        print("Utente non trovato.")
        return False
    
    if data[email] == password:
        print("Login effettuato con successo.")
        return True
    else:
        print("Password errata.")
        return False

