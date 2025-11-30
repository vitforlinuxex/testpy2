import random
def gara_sci_fondo(nazioni, team_atleti, impianti, assegna_medaglie):
    print(f"\nEvento: Sci fondo ({impianti['pista_sci']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["sci"]:
            tempo = round(random.uniform(1800, 2400), 2)  # 30-40 minuti in secondi
            risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)

