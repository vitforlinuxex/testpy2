"""
vorrei fare una funzione in python che invii i dati di una variabile in un file .txt nella cartella dell utente corrente
"""
from pathlib import Path

def scrivi_su_file_nella_home(nome_file, dati):
    home_dir = Path.home()
    percorso_file = home_dir / nome_file
    
    with percorso_file.open('w', encoding='utf-8') as file:
        file.write(str(dati))
    
    print(f"Dati scritti in: {percorso_file}")