import random

def gioca_roulette(num_giri):
    # Numeri della roulette francese (0-36)
    numeri = list(range(37))
    
    # Inizializzazione contatori
    numeri_pari = [num for num in numeri if num % 2 == 0]
    conteggio_pari = 0
    
    # Simulazione giri
    risultati = []
    for _ in range(num_giri):
        numero_uscito = random.choice(numeri)
        risultati.append(numero_uscito)
        if numero_uscito in numeri_pari:
            conteggio_pari += 1
            
    # Calcolo percentuale
    percentuale_pari = (conteggio_pari / num_giri) * 100
    
    return {
        'numero_giri': num_giri,
        'conteggio_pari': conteggio_pari,
        'percentuale_pari': round(percentuale_pari, 2),
        'risultati': risultati
    }

# Esempio di utilizzo con 100 giri
risultato = gioca_roulette(100)

print(f"Dopo {risultato['numero_giri']} giri:")
print(f"Numeri pari usciti: {risultato['conteggio_pari']}")
print(f"Percentuale numeri pari: {risultato['percentuale_pari']}%")
print("\nUltimi 10 numeri usciti:", risultato['risultati'][-10:])