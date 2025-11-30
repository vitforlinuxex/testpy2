import random
def gara_pattinaggio_artistico(nazioni, team_atleti, impianti, assegna_medaglie):
    print(f"\nEvento: Pattinaggio artistico (mattina) ({impianti['palaghiaccio']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["artistico"]:
            punteggio = round(random.uniform(50, 100), 2)
            risultati.append({"nazione": nazione, "atleta": atleta, "punteggio": punteggio})
    assegna_medaglie(risultati, "punteggio")