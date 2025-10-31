import tkinter as tk

def mostra_finestra(titolo, testo):
    root = tk.Tk()
    root.title(titolo)  # Imposta il titolo della finestra

    label = tk.Label(root, text=testo)
    label.pack(padx=40, pady=40)

    btn_chiudi = tk.Button(root, text="Chiudi", command=root.destroy)
    btn_chiudi.pack(pady=(0, 20))

    root.mainloop()
    
def albero_natale(altezza):
	alberon=""
	for i in range(altezza):
	# Spazi per centrare gli asterischi
		alberon += (' ' * (altezza - i - 2) + '*' * (2 * i + 1) + "\n")
	# Tronco dell'albero
	for j in range(altezza // 3):
		alberon += (' ' * (altezza - 5) + '**'+ "\n")
	return alberon

# Esempio di utilizzo
titolo_finestra = "Buon Natale"
altezza_albero = 7
#albero_natale(altezza_albero)
testo_da_mostrare = albero_natale(altezza_albero)

mostra_finestra(titolo_finestra, testo_da_mostrare)