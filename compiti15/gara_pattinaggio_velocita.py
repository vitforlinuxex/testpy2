import random
def gara_pattinaggio_velocita(nazioni, team_atleti, impianti, assegna_medaglie):
    print(f"\nEvento: Pattinaggio velocità (mattina) ({impianti['palaghiaccio']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["velocità"]:
            tempo = round(random.uniform(30, 55), 2)
            risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)