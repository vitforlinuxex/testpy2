import random
def gara_sci_discesa(nazioni, team_atleti, impianti, assegna_medaglie):
    print(f"\nEvento: Sci discesa ({impianti['pista_sci']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["sci"]:
            tempo = round(random.uniform(40, 70),2)
            risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)