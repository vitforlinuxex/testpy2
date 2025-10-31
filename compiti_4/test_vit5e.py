#!/usr/bin/env python3

import numpy as np
np.set_printoptions(legacy='1.25')
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

dati_gui1=""

def mostra_finestra(titolo, testo):
    root = ThemedTk(theme="keramik")
    root.title(titolo)  # Imposta il titolo della finestra

    label = ttk.Label(root, text=testo)
    label.pack(padx=20, pady=20)

    btn_chiudi = ttk.Button(root, text="Chiudi", command=root.destroy).pack()
    #btn_chiudi.pack(pady=(0, 20))

    root.mainloop()

dati = [10,20,30,40,50]

def M1(x):
    z=x*2
    return z

def M2(x):
    z = np.square(x)
    return z

def M3(x):
    z=np.add(x,2)
    return z

def test_modelli_Mi(lista,funzione):
    nuova_lista = []
    for i in lista:
        nuova_lista.append(funzione(i))
    return nuova_lista
    
#print(test_modelli_Mi(dati,M1))
#print(test_modelli_Mi(dati,M2))
#print(test_modelli_Mi(dati,M3))
#dati_gui1=(test_modelli_Mi(dati,M1))

def score_models(actual_model, expected_models):
    def calculate_score(model):
        differences = [abs(a - b) ** 2 for a, b in zip(actual_model, model)]
        return sum(differences)
    
    scores = {name: calculate_score(expected_model) for name, expected_model in expected_models.items()}
    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    return dict(sorted_scores)

# Esempio d'uso:
real_model = [18,33,56,73,110]
known_models = {
    'Modello 1': M1(dati),
    'Modello 2': M2(dati),
    'Modello 3': M3(dati)
}

result = score_models(real_model, known_models)

#print(result)
titolo_finestra="Risultato calcolo"
#(test_modelli_Mi(dati,M1))
testo_da_mostrare = f"Dati Reali: {real_model}\n\n Modello 1: {(test_modelli_Mi(dati,M1))}\nModello 2: {(test_modelli_Mi(dati,M2))}\n Modello 3: {(test_modelli_Mi(dati,M3))}\n\nRisultato :{result}"
mostra_finestra(titolo_finestra, testo_da_mostrare)
