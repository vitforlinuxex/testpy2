import tkinter as tk

def mostra_finestra(titolo, testo):
    root = tk.Tk()
    root.title(titolo)  # Imposta il titolo della finestra

    label = tk.Label(root, text=testo)
    label.pack(padx=20, pady=20)

    btn_chiudi = tk.Button(root, text="Chiudi", command=root.destroy)
    btn_chiudi.pack(pady=(0, 20))

    root.mainloop()

# Esempio di utilizzo:
titolo_finestra = "Titolo della mia finestra"
testo_da_mostrare = "Questo è il testo mostrato automaticamente appena si apre la finestra."

mostra_finestra(titolo_finestra, testo_da_mostrare)
