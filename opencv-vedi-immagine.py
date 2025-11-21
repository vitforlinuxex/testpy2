import cv2

# Carica l'immagine dal file
#C:\Users\Studente\Downloads\steampunk-starshipAI5.jpg
immagine = cv2.imread('C:/Users/Studente/Downloads/steampunk-starshipAI5.jpg')

# Controlla che l'immagine sia stata caricata correttamente
if immagine is None:
    print("Errore: impossibile caricare l'immagine.")
else:
    # Mostra l'immagine in una finestra
    cv2.imshow('Immagine', immagine)

    # Aspetta la pressione di un tasto per chiudere la finestra
    cv2.waitKey(0)