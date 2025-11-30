def stampa_medagliere(nazioni, medagliere):
    print("\nMedagliere finale:")
    print(f"{'Nazione':12s} {'Oro':>4s} {'Argento':>8s} {'Bronzo':>7s} {'Totale':>7s}")
    for n in nazioni:
        oro = medagliere[n]["Oro"]
        arg = medagliere[n]["Argento"]
        bro = medagliere[n]["Bronzo"]
        tot = oro + arg + bro
        print(f"{n:12s} {oro:4d} {arg:8d} {bro:7d} {tot:7d}")