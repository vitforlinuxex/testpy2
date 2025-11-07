def controlla_nome_utente(nome_utente):
    """
    Controlla se il nome utente contiene almeno una '@' e un '.'

    Args:
        nome_utente (str): il nome utente da controllare

    Returns:
        bool: True se contiene almeno una '@' e un '.', False altrimenti
    """
    return '@' in nome_utente and '.' in nome_utente

#nome = input("inserisci nome utente tipo \"nome@dominio.com\" \n ")
#print(controlla_nome_utente(nome))  # Output: True

def controlla_stringa(s):
    """
    Controlla se la stringa contiene almeno un '*' e non contiene parentesi '(' o ')'

    Args:
        s (str): la stringa da controllare

    Returns:
        bool: True se la stringa rispetta le condizioni, False altrimenti
    """
    return len(s) >= 8 and '*' in s and '(' not in s and ')' not in s

# Esempi di utilizzo:
#print(controlla_stringa("esempio*stringa"))   # True
#print(controlla_stringa("esempio(stringa)"))  # False
#print(controlla_stringa("esempio stringa"))   # False
#print(controlla_stringa("esempio*stringa("))  # False

nome = input("inserisci nome utente tipo \"nome@dominio.com\" \n ")
print(controlla_nome_utente(nome))  # Output: True

password = input("inserisci password che contenga \* e non contenga \( \) \n ")

print(controlla_stringa(password))