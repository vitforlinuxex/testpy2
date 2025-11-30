"""
Devo fare un gioco didattico in python che si svolga nel terminale a tema olimiadi invernali, 
ci sono quattro squadre di quattro nazioni: Italia, Francia, Spagna e Germania con 6 hockeisti, 
2 pattinatori artistici, 2 pattinatori velocisti, 2 sciatori, 2 bobbisti maschi e 2 bobbiste femine 
che fanno 4 gare al giorno per 4 giorni in tre impianti: la pista di bob, la pista di sci e il palaghiaccio 
ci sono tre impianti: pista di sci, pista di bob e palaghiaccio che non può avere più di due eventi al giorno, 
uno alla mattina e uno alla sera e verrà undicato a fianco della gara
- gli atleti devono avere dei nomi buffi con uno spazio tra nome e cognome adatti alla nazione
- gli impianti devono avere nomi buffi
- le gare di sci avvengono sulla pista di sci, slittino e bob sulla pista da bob
- nelle due gare di pattinaggio, artistico e velocità possono partecipare al massimo due atleti per nazione
- nel pattinaggio artistico chi ha punteggio più alto vince
- nella gara di pattinaggio velocità chi ha tempo minore vince
- non ci possono essere gare di pattinaggio durante le gare di hockey e due gare di hockey contemporaneamente,
  saranno sempre una di sera e una al mattino, e deve sempre essere indicato se la partita è di sera o di mattino
- nello sci salto chi raggiunge maggiore distanza in metri vince
- nella gara di sci discesa chi ha tempo minore vince
- usa uno dei bobbisti maschi per la gara di slittino maschi
- usa una delle bobbiste femmine le la gara di slittino femmine
- oltre al medagliere per ogni gara verranno indicati anche i tempi o punteggi di chi non ha vinto
- indica le medaglie con Oro, Argento e Bronzo anche nelle gare
- alla fine verrà indicato un medagliere che indichi quante medaglie ha vinto ogni nazione
- questo prompt deve essere aggiunto al programma in un commento multilinea senza modifiche
- Calendario:

1 giorno

sci-discesa
slittino uomini
pattinaggio-velocità (mattina)
hockey 1 contro 2 (sera)

2 giorno

sci-slalom
bob a due a due uomini
pattinaggio artistico singolo (mattina)
hockey 3 contro 4 (sera)

3 giorno

sci-salto
bob a due donne
hockey vincente prima partita contro vincente seconda partita orario (mattina)
hockey perdente prima partita contro perdente seconda partita orario (sera)

4 giorno
sci fondo
slittino donne
hockey vincente prima partita 3 giorno contro vincente 3 giorno seconda partita (mattina)

premiazione
"""

import random

# Atleti buffi (nome con cognome separati da spazio)
nazioni = ["Italia", "Francia", "Spagna", "Germania"]

team_atleti = {
    "Italia": {
        "hockey": ["Pinguino Pippo", "Ciao Mario", "Gelato Gino", "Baffo Nino", "Bombolone Luca", "Pizza Alfredo"],
        "artistico": ["Dolce Luca", "Bello Marco"],
        "velocità": ["Flash Vanni", "ZigZag Totò"],
        "sci": ["Neve Paolo", "Slalom Gianni"],
        "bobbisti_m": ["Turbo Mario", "Vento Luca"],
        "bobbiste_f": ["Vesuvia Anna", "Ghiaccia Rosa"],
    },
    "Francia": {
        "hockey": ["Fromage Jean", "Baguette Pierre", "Croissant Luc", "Escargot Henri", "Beret Louis", "Macaron Paul"],
        "artistico": ["Belle Amelie", "Fleur Marie"],
        "velocità": ["Rapide Jean", "Vite Pierre"],
        "sci": ["Glace Claude", "Piste Louis"],
        "bobbisti_m": ["Rapide Henri", "Foudre Paul"],
        "bobbiste_f": ["Neige Claire", "Glisse Marie"],
    },
    "Spagna": {
        "hockey": ["Tapa Jose", "Fiesta Carlos", "Sombrero Miguel", "Sangria Luis", "Churro Alberto", "Flamenco Juan"],
        "artistico": ["Linda Sofia", "Rosa Marta"],
        "velocità": ["Rayo Carlos", "Veloz Juan"],
        "sci": ["Blanco Rafael", "Pico Diego"],
        "bobbisti_m": ["Rayo Jose", "Trueno Luis"],
        "bobbiste_f": ["Luna Marta", "Estrella Sofia"],
    },
    "Germania": {
        "hockey": ["Pretzel Hans", "Bratwurst Kurt", "Bier Fritz", "Sauerkraut Otto", "Schnitzel Max", "Gretel Wolf"],
        "artistico": ["Schnee Anna", "Gretel Elsa"],
        "velocità": ["Schnell Hans", "Flitz Otto"],
        "sci": ["Berg Otto", "Schnee Klaus"],
        "bobbisti_m": ["Blitz Hans", "Donner Fritz"],
        "bobbiste_f": ["Schnee Elsa", "Eis Greta"],
    },
}

# Impianti buffi
impianti = {
    "pista_sci": "Montagna Pazza",
    "pista_bob": "Ghiaccio Volante",
    "palaghiaccio": "Palagelatissimo",
}

# Medagliere
medagliere = {n: {"Oro": 0, "Argento": 0, "Bronzo": 0} for n in nazioni}

def stampa_medagliere():
    print("\nMedagliere finale:")
    print(f"{'Nazione':12s} {'Oro':>4s} {'Argento':>8s} {'Bronzo':>7s} {'Totale':>7s}")
    for n in nazioni:
        oro = medagliere[n]["Oro"]
        arg = medagliere[n]["Argento"]
        bro = medagliere[n]["Bronzo"]
        tot = oro + arg + bro
        print(f"{n:12s} {oro:4d} {arg:8d} {bro:7d} {tot:7d}")

def assegna_medaglie(risultati, chiave, inverti=False, atleta_key="atleta"):
    if inverti:
        risultati.sort(key=lambda x: x[chiave])
    else:
        risultati.sort(key=lambda x: x[chiave], reverse=True)
    print("Classifica:")
    for i, r in enumerate(risultati[:10], start=1):
        medaglia = None
        if i == 1: medaglia = "Oro"
        elif i == 2: medaglia = "Argento"
        elif i == 3: medaglia = "Bronzo"

        if medaglia:
            medagliere[r["nazione"]][medaglia] += 1

        atleta = r[atleta_key]
        if isinstance(atleta, list):
            atleta = " e ".join(atleta)
        val = r[chiave]
        unità = "s" if chiave == "tempo" else " punti" if chiave == "punteggio" else " metri" if chiave == "distanza" else ""
        print(f"{i}. {atleta} ({r['nazione']}) - {val}{unità} - {medaglia if medaglia else ''}")

def gara_sci_discesa():
    print(f"\nEvento: Sci discesa ({impianti['pista_sci']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["sci"]:
            tempo = round(random.uniform(40, 70),2)
            risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)

def gara_slittino_uomini():
    print(f"\nEvento: Slittino uomini ({impianti['pista_bob']})")
    risultati = []
    for nazione in nazioni:
        atleta = team_atleti[nazione]["bobbisti_m"][0]
        tempo = round(random.uniform(40, 70), 2)
        risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)

def gara_pattinaggio_velocita():
    print(f"\nEvento: Pattinaggio velocità (mattina) ({impianti['palaghiaccio']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["velocità"]:
            tempo = round(random.uniform(30, 55), 2)
            risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)

def hockey_partita(squadra1, squadra2, momento):
    print(f"\nPartita hockey {momento}: {squadra1} vs {squadra2} ({impianti['palaghiaccio']})")
    punteggio1, punteggio2 = 0, 0
    dettagli1, dettagli2 = [], []
    for giocatore in team_atleti[squadra1]["hockey"]:
        gol = random.randint(0, 3)
        punteggio1 += gol
        dettagli1.append((giocatore, gol))
    for giocatore in team_atleti[squadra2]["hockey"]:
        gol = random.randint(0, 3)
        punteggio2 += gol
        dettagli2.append((giocatore, gol))
    print(f"Risultato: {squadra1} {punteggio1} - {punteggio2} {squadra2}")
    print(f"Dettagli {squadra1}: " + ", ".join(f"{g[0]}({g[1]} gol)" for g in dettagli1))
    print(f"Dettagli {squadra2}: " + ", ".join(f"{g[0]}({g[1]} gol)" for g in dettagli2))
    if punteggio1 > punteggio2:
        return squadra1
    elif punteggio2 > punteggio1:
        return squadra2
    else:
        rigori1, rigori2 = random.randint(0,3), random.randint(0,3)
        print(f"Pareggio, rigori: {rigori1} - {rigori2}")
        if rigori1 != rigori2:
            return squadra1 if rigori1 > rigori2 else squadra2
        else:
            vincitore = random.choice([squadra1, squadra2])
            print(f"Vincitore ai rigori (random): {vincitore}")
            return vincitore

def gara_sci_slalom():
    print(f"\nEvento: Sci slalom ({impianti['pista_sci']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["sci"]:
            tempo = round(random.uniform(50, 90),2)
            risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)

def gara_bob_uomini():
    print(f"\nEvento: Bob a due uomini ({impianti['pista_bob']})")
    risultati = []
    for nazione in nazioni:
        coppia = team_atleti[nazione]["bobbisti_m"][:2]
        tempo = round(random.uniform(35, 60),2)
        risultati.append({"nazione": nazione, "atleta": coppia, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True, atleta_key="atleta")

def gara_pattinaggio_artistico():
    print(f"\nEvento: Pattinaggio artistico (mattina) ({impianti['palaghiaccio']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["artistico"]:
            punteggio = round(random.uniform(50, 100), 2)
            risultati.append({"nazione": nazione, "atleta": atleta, "punteggio": punteggio})
    assegna_medaglie(risultati, "punteggio")

def gara_sci_salto():
    print(f"\nEvento: Sci salto ({impianti['pista_sci']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["sci"]:
            distanza = round(random.uniform(70, 140), 2)
            risultati.append({"nazione": nazione, "atleta": atleta, "distanza": distanza})
    assegna_medaglie(risultati, "distanza")

def gara_bob_donne():
    print(f"\nEvento: Bob a due donne ({impianti['pista_bob']})")
    risultati = []
    for nazione in nazioni:
        coppia = team_atleti[nazione]["bobbiste_f"][:2]
        tempo = round(random.uniform(38, 65), 2)
        risultati.append({"nazione": nazione, "atleta": coppia, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True, atleta_key="atleta")

def gara_sci_fondo():
    print(f"\nEvento: Sci fondo ({impianti['pista_sci']})")
    risultati = []
    for nazione in nazioni:
        for atleta in team_atleti[nazione]["sci"]:
            tempo = round(random.uniform(1800, 2400), 2)  # 30-40 minuti in secondi
            risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)

def gara_slittino_donne():
    print(f"\nEvento: Slittino donne ({impianti['pista_bob']})")
    risultati = []
    for nazione in nazioni:
        atleta = team_atleti[nazione]["bobbiste_f"][0]
        tempo = round(random.uniform(42, 75), 2)
        risultati.append({"nazione": nazione, "atleta": atleta, "tempo": tempo})
    assegna_medaglie(risultati, "tempo", inverti=True)

def main():
    print("Benvenuti alle Olimpiadi Invernali buffe!")

    # Giorno 1
    print("\n--- Giorno 1 ---")
    gara_pattinaggio_velocita()
    gara_sci_discesa()
    gara_slittino_uomini()
    vincitore1 = hockey_partita(nazioni[0], nazioni[1], "sera")

    # Giorno 2
    print("\n--- Giorno 2 ---")
    gara_pattinaggio_artistico()
    gara_sci_slalom()
    gara_bob_uomini()
    vincitore2 = hockey_partita(nazioni[2], nazioni[3], "sera")

    # Giorno 3
    print("\n--- Giorno 3 ---")
    gara_sci_salto()
    gara_bob_donne()
    vincitore_mattina = hockey_partita(vincitore1, vincitore2, "mattina")
    perdente1 = nazioni[0] if vincitore1 != nazioni[0] else nazioni[1]
    perdente2 = nazioni[2] if vincitore2 != nazioni[2] else nazioni[3]
    vincitore_sera = hockey_partita(perdente1, perdente2, "sera")

    # Giorno 4
    print("\n--- Giorno 4 ---")
    vincitore_finale = hockey_partita(vincitore_mattina, vincitore_sera, "mattina")
    gara_sci_fondo()
    gara_slittino_donne()

    stampa_medagliere()
    print(f"\nCampione finale hockey: {vincitore_finale}")

if __name__ == "__main__":
    main()
