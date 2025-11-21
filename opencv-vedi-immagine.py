import cv2
while True:
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
        tasto = cv2.waitKey(1)
        if tasto==ord("q"):
            break
        elif tasto==ord("a"):
            cv2.imwrite("foto.jpg",immagine)
            
cv2.destroyAllWindows()
    