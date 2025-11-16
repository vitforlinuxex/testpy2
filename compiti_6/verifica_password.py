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