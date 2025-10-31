import numpy as np
np.set_printoptions(legacy='1.25')

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
    
print(test_modelli_Mi(dati,M1))
print(test_modelli_Mi(dati,M2))
print(test_modelli_Mi(dati,M3))

def score_models(actual_model, expected_models):
    def calculate_score(model):
        differences = [abs(a - b) ** 2 for a, b in zip(actual_model, model)]
        return sum(differences)
    
    scores = {name: calculate_score(expected_model) for name, expected_model in expected_models.items()}
    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    return dict(sorted_scores)

# Esempio d'uso:
actual_model = [18,33,56,73,110]
expected_models = {
    'Modello 1': M1(dati),
    'Modello 2': M2(dati),
    'Modello 3': M3(dati)
}

result = score_models(actual_model, expected_models)

print(result)
