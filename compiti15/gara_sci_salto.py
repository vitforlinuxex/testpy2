import random
def gara_sci_salto(nazioni, team_atleti, impianti, assegna_medaglie):
    print(f"\nEvento: Sci salto ({impianti['pista_sci']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["sci"]:
            distanza = round(random.uniform(70, 140), 2)
            risultati.append({"nazione": nazione, "atleta": atleta, "distanza": distanza})
    assegna_medaglie(risultati, "distanza")