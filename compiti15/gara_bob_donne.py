import random
def gara_bob_donne(nazioni, team_atleti, impianti, assegna_medaglie):
    print(f"\nEvento: Bob a due donne ({impianti['pista_bob']})")
    risultati = []
    for nazione in nazioni:
        coppia = team_atleti[nazione]["bobbiste_f"][:2]
        tempo = round(random.uniform(38, 65), 2)
        risultati.append({"nazione": nazione, "atleta": coppia, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True, atleta_key="atleta")