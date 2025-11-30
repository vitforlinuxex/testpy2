import random
def gara_bob_uomini(nazioni, team_atleti, impianti, assegna_medaglie):
    print(f"\nEvento: Bob a due uomini ({impianti['pista_bob']})")
    risultati = []
    for nazione in nazioni:
        coppia = team_atleti[nazione]["bobbisti_m"][:2]
        tempo = round(random.uniform(35, 60),2)
        risultati.append({"nazione": nazione, "atleta": coppia, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True, atleta_key="atleta")