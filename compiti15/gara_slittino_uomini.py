import random
def gara_slittino_uomini(nazioni, team_atleti, impianti, assegna_medaglie):
    print(f"\nEvento: Slittino uomini ({impianti['pista_bob']})")
    risultati = []
    for nazione in nazioni:
        atleta = team_atleti[nazione]["bobbisti_m"][0]
        tempo = round(random.uniform(40, 70), 2)
        risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)