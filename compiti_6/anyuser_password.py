import anyjson
import os

FILE_NAME = 'user_password.json'

def save_user(username, password):
    # Crea l'email dall'username
    email = f"{username}"
    
    # Controlla se il file esiste, altrimenti crea un dizionario vuoto
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            users = anyjson.deserialize(f.read())
    else:
        users = {}
    
    # Salva o aggiorna l'utente in chiaro
    users[email] = password
    
    # Salva il file aggiornato in formato JSON
    with open(FILE_NAME, 'w') as f:
        f.write(anyjson.serialize(users))
        
    print(f"Utente {email} salvato con password in chiaro.")

def check_login(username, password):
    email = f"{username}"
    if not os.path.exists(FILE_NAME):
        return False
    with open(FILE_NAME, 'r') as f:
        users = anyjson.deserialize(f.read())
    
    if email in users and users[email] == password:
        return True
    else:
        return False
