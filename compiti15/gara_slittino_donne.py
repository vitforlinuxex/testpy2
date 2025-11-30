import random
def gara_slittino_donne(nazioni, team_atleti, impianti, assegna_medaglie):
    print(f"\nEvento: Slittino donne ({impianti['pista_bob']})")
    risultati = []
    for nazione in nazioni:
        atleta = team_atleti[nazione]["bobbiste_f"][0]
        tempo = round(random.uniform(42, 75), 2)
        risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)