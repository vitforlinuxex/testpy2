# ------------  SVILUPPATORE 3) --------------
import scrivi_su_file_nella_home


"""
crea una funzione in python che controlli se un nome utente nella forma di un indirizzo email non è nalla lista contenuta nella funzione con 10 indirizzi email di fantasia e se nell indirizzo email sono contenuti una chiocciola e un punto
"""

"""
#crea una funzione in python per il controllo di una stringa, deve contenere almeno 8 caratteri, numeri e lettere, almeno una Maiuscola, almeno un carattere speciale a scelta tra ".,-_#!?%&$", non  deve contenere",/,\,(),{},[]"
"""
print("Benvenuto nella pagina di ingresso al nostro sito.\nSe vuoi Registrarti premi 1 se vuoi fare login premi 2")

login = int(input())
import _9_2_verifica_requisiti
import scrivi_su_file_nella_home

if login == 1:
    print("Benvenuto nella pagina di iscrizione al nostro sito.\nPer registrarti dovrai scegliere uno username inserendo la tua email e una password che rispetti i seguenti requisiti:")
    print("\t\tAlmeno 8 caratteri\n\t\tSia numeri che lettere\n\t\tAlmeno una Maiuscola\n\t\tAlmeno un carattere speciale a scelta tra .,-_#!?%&$\n\t\tNon sono consentiti i seguenti caratteri \\/\\,\\(\\)\\{\\}\\[\\]")

    while True:
        user = input("Scegli il nome utente: \n\t")
        if _9_2_verifica_requisiti.verifica_user(user): break
        else: print("Attenzione, inserire una email valida!")

    password = input("Scegli la tua password: \n\t")
    while not _9_2_verifica_requisiti.verifica_password(password):
        print("Attenzione, la password non rispetta i requisiti richiesti. Sceglierne una nuova.") 
        password = input("Scegli la tua password \n\t")

    import anyuser_password
    anyuser_password.save_user(user, password)

    print("User e password rispettano i requisiti.\nTi verrà inviata una email con il riepilogo dei dati di login. \nOra verrai reindirizzato alla schermata di login.")
    print(f"\n\n*-------------------------*\nDati di Login:\n\t\tUsername:\t{user}\n\t\tPassword:\t{password}\n*-------------------------*")
    variabile = f"\n\n*-------------------------*\nDati di Login:\n\t\tUsername:\t{user}\n\t\tPassword:\t{password}\n*-------------------------*"
    scrivi_su_file_nella_home.scrivi_su_file_nella_home("user_pass_output_"+user+".txt", variabile)

# e la registrazione è fatta... ora pensiamo al login
if login == 2:
    import anyuser_password
    while True:
        print("Ora devi fare Login... ma chi tel'ha fatto fare?\n")
        user = input("Nome utente nella forma user@domain.com\n")
        password = input("\nPassword... e qui sono cavoli\n")
        controllo = anyuser_password.check_login(user, password)
        if controllo == 1 : print("Evvai!")
        else: print("Attenzione, inserire una email registrata oppure registrati!")

    
        
        
        




    

"""
#
# per fini didattici la verifica sullo user la facciamo con un ciclo while, mentre la verifica sulla password
# la facciamo simulando un do-while
#
"""

#------------SVILUPPATORE 4)-------------

# Ripasso sintassi ciclo while:
# while condizione True:
#   espressioni o istruzioni
