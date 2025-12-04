"""
Vorrei un gioco tipo dungenos and dragons in python per il terminale, ci sono 4 personaggi, due maghi che sono nemici tra loro il primo di nome
 Dario e il secondo Luigi, un guerriero di nome Baldo amico di Dario e un troll che si danno battaglia, aggiungi un dado per regolare la potenza
 degli effetti
- il mago Dario ha la bacchetta dei fulmini che quando viene usata fa "Zzzzzott!!" come scritta nel terminale e può fare controincantesimi, e
 quando li fa appare la scritta "Ti ho fregato!" nel terminale, ma può usare la magia solo se ha sufficente potere magico,  ha vitalita 30 e
 magia 10
- il mago Luigi può fare incantesimi e accecare il Guerriero Baldo solo se ha sufficente potere magico ha vitalita 30 e magia 10
- il Troll ha vitalità 50 e può essere maledetto e dopo avere meno forza
- Il guerriero Baldo ha una spada che se accecato usa con meno abilità, ma il mago Dario può guarirlo con un controincantesimo, ha vitalita 50
- aggiungi un dado per regolare la potenza degli effetti, il numero estratto del dado si vedrà a ogni partita
- usa variabili e nomi di funzioni in italiano quando possibile
- inserisci questo prompt in un commento multilinea senza modificarlo
- al mago Dario farà piacere se usi parte del codice qui sotto, anche se lo modifichi:

import random
class Incantatore:
    pass
class Stregone(Incantatore):
    pass

class Spada:
    def uso_spada(self,utilizzatore,nemico):
        if getattr(utilizzatore,"cecita","Non Cieco")=="Cieco":
            nemico.vitalita -= 5
        else:
            nemico.vitalita -= 10

class Bacchetta_dei_fulmini:
    def uso_bacchetta(self,utilizzatore, nemico):
        if isinstance(utilizzatore,Incantatore):
            print("Zzzzzott!!")
            nemico.vitalita -= 20
        else:
            print("Non puoi utilizzare la bacchetta")

class Guerriero:
    def __init__(self,nome,vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.maledetto = False

class Mago(Incantatore):
    def __init__(self,nome,vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.slot_incantesimo = 10
        self.maledetto = False
    def palla_di_fuoco(self,other):
        if self.slot_incantesimo >0:
            if not hasattr(other,"controincantesimo"):
                other.vitalita -= random.randint(5,40)
            else:
                other.controincantesimo()
        self.slot_incantesimo -=1
    def controincantesimo(self): # annulla l'effetto dell'incantesimo
        print("Ti ho fregato!")
        self.slot_incantesimo -=1
    def cura_ferite(self,other):
        other.vitalita += 10
        self.slot_incantesimo -=1
    def maledizione(self, other):
        setattr(other,"maledetto",True)
        self.slot_incantesimo -=1
    def cecita(self, other):
        other.cecita = "Cieco" # aggiungo uno stato di cecità solo 
        # all'istanza che riceve questo incantesimo e gliela aggiungo
        # come attributo di singola istanza.
        self.slot_incantesimo -=1
    def cura_cecita(self,other):
        if hasattr(other,"cecita"):
            delattr(other,"cecita")
        self.slot_incantesimo -=1
        

    def __str__(self):
        return f"*-----------*\nScheda di {self.nome}:\npunti vita: {self.vitalita}\nMagia: {self.slot_incantesimo} \n*-----------*"


class Troll:
    def __init__(self,nome,vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.maledetto = False

protagonista = Mago("Dario",30)
protagonista2 = Guerriero("Baldo",40)
nemico1 = Mago("Luigi",25)
nemico2 = Troll("Troll",50)
bacchetta = Bacchetta_dei_fulmini()
spada = Spada()

print("*-----------*\n", protagonista.nome,"Vitalità",protagonista.vitalita,"Magia",protagonista.slot_incantesimo,"\n*-----------*")
print("*-----------*\n", protagonista2.nome,"Vitalità",protagonista2.vitalita,"\n*-----------*")
print("*-----------*\n", nemico1.nome,"Vitalità",nemico1.vitalita,"Magia",nemico1.slot_incantesimo,"\n*-----------*")
print("*-----------*\n", nemico2.nome,"Vitalità",nemico2.vitalita,"\n*-----------*")
"""

import random
import time

class Incantatore:
    pass

class Stregone(Incantatore):
    pass

class Spada:
    def uso_spada(self, utilizzatore, nemico, potenza):
        if getattr(utilizzatore, "cecita", "Non Cieco") == "Cieco":
            danno = 5 + potenza
        else:
            danno = 10 + potenza
        nemico.vitalita -= danno
        print(f"{utilizzatore.nome} colpisce con la spada causando {danno} danni a {nemico.nome}.")

class Bacchetta_dei_fulmini:
    def uso_bacchetta(self, utilizzatore, nemico, potenza):
        if isinstance(utilizzatore, Incantatore):
            if utilizzatore.slot_incantesimo >= 2:
                print("Zzzzzott!!")
                danno = 15 + potenza
                nemico.vitalita -= danno
                utilizzatore.slot_incantesimo -= 2
                print(f"{utilizzatore.nome} usa la bacchetta e infligge {danno} danni a {nemico.nome}.")
            else:
                print(f"{utilizzatore.nome} non ha abbastanza potere magico per usare la bacchetta!")
        else:
            print("Non puoi utilizzare la bacchetta")

class Guerriero:
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.maledetto = False

    def __str__(self):
        stato = f"Cieco" if hasattr(self, "cecita") and self.cecita == "Cieco" else "Normale"
        maledetto = "Maledetto" if self.maledetto else "Normale"
        return f"*-----------*\nGuerriero {self.nome}:\nVitalità: {self.vitalita}\nStato: {stato}\nMaledizione: {maledetto}\n*-----------*"

class Mago(Incantatore):
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.slot_incantesimo = 10
        self.maledetto = False

    def incantesimo_fuoco(self, other, potenza):
        if self.slot_incantesimo >= 1:
            danno = random.randint(5, 15) + potenza
            if not hasattr(other, "controincantesimo"):
                other.vitalita -= danno
                print(f"{self.nome} lancia palla di fuoco su {other.nome}, infliggendo {danno} danni.")
            else:
                other.controincantesimo()
            self.slot_incantesimo -=1
        else:
            print(f"{self.nome} non ha abbastanza potere magico per lanciare palla di fuoco.")

    def controincantesimo(self):
        print("Ti ho fregato!")
        if self.slot_incantesimo > 0:
            self.slot_incantesimo -=1

    def cura_ferite(self, other, potenza):
        if self.slot_incantesimo >= 2:
            cura = 10 + potenza
            other.vitalita += cura
            print(f"{self.nome} cura {other.nome} di {cura} punti vita.")
            self.slot_incantesimo -= 2
        else:
            print(f"{self.nome} non ha abbastanza magia per curare.")

    def maledizione(self, other, potenza):
        if self.slot_incantesimo >= 2:
            setattr(other, "maledetto", True)
            other.vitalita -= (5 + potenza)
            print(f"{self.nome} maledice {other.nome}! Vitalità diminuita e maledetto.")
            self.slot_incantesimo -= 2
        else:
            print(f"{self.nome} non ha abbastanza magia per maledire.")

    def cecita(self, other, potenza):
        if self.slot_incantesimo >= 3:
            other.cecita = "Cieco"
            print(f"{self.nome} acceca {other.nome}! Ora è cieco.")
            self.slot_incantesimo -= 3
        else:
            print(f"{self.nome} non ha abbastanza magia per accecare.")

    def cura_cecita(self, other):
        if self.slot_incantesimo >= 2:
            if hasattr(other, "cecita"):
                delattr(other, "cecita")
                print(f"{self.nome} rimuove la cecità da {other.nome}.")
            else:
                print(f"{other.nome} non è cieco.")
            self.slot_incantesimo -= 2
        else:
            print(f"{self.nome} non ha abbastanza magia per rimuovere la cecità.")

    def __str__(self):
        maledetto = "Maledetto" if self.maledetto else "Normale"
        return f"*-----------*\nScheda di {self.nome}:\nPunti vita: {self.vitalita}\nMagia: {self.slot_incantesimo}\nMaledizione: {maledetto}\n*-----------*"

class Troll:
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.maledetto = False

    def __str__(self):
        maledetto = "Maledetto" if self.maledetto else "Normale"
        return f"*-----------*\nTroll {self.nome}:\nVitalità: {self.vitalita}\nMaledizione: {maledetto}\n*-----------*"

def stampa_stato(personaggi):
    for p in personaggi:
        print(p)

def lancio_dado():
    dado = random.randint(1,6)
    print(f"\nIl dado è caduto su: {dado}\n")
    return dado

def turno_dario(dario, baldo, luigi, troll, bacchetta, spada, dado):
    # Dario può scegliere di usare bacchetta, controincantesimo o curare Baldo o attaccare normale.
    print(f"Turno di {dario.nome}")
    print(dario)
    print(baldo)
    print(luigi)
    print(troll)
    azioni_possibili = ['1: Usa bacchetta sui nemici',
                        '2: Controincantesimo su Luigi',
                        '3: Cura Baldo',
                        '4: Attacca Troll con spada']
    print("Azioni possibili:")
    for az in azioni_possibili:
        print(az)
    scelta = input("Scegli azione (1-4): ").strip()
    if scelta == '1':
        # bacchetta sui nemici: scegli uno
        if dario.slot_incantesimo < 2:
            print(f"{dario.nome} non ha abbastanza magia per usare la bacchetta.")
            return
        print("Scegli bersaglio (1) Luigi, (2) Troll")
        bersaglio = input("Scelta bersaglio: ").strip()
        if bersaglio == '1':
            bacchetta.uso_bacchetta(dario, luigi, dado)
        elif bersaglio == '2':
            bacchetta.uso_bacchetta(dario, troll, dado)
        else:
            print("Bersaglio non valido.")
    elif scelta == '2':
        # controincantesimo su Luigi
        if dario.slot_incantesimo < 1:
            print(f"{dario.nome} non ha abbastanza magia per controincantesimo.")
            return
        # Qui controincantesimo è attivato probabilmente come reazione a incantesimo nemico, 
        # ma per il gioco semplice possiamo decidere di attivare la funzione su Luigi.
        print(f"{dario.nome} tenta controincantesimo su {luigi.nome}.")
        luigi.controincantesimo()
    elif scelta == '3':
        # cura Baldo
        dario.cura_ferite(baldo, dado)
    elif scelta == '4':
        # attacca troll con spada
        spada.uso_spada(dario, troll, dado)
    else:
        print("Azione non valida, turno perso.")

def turno_luigi(luigi, baldo, dario, troll, dado):
    print(f"Turno di {luigi.nome}")
    print(luigi)
    print(baldo)
    print(dario)
    print(troll)
    azioni_possibili = ['1: Lancia incantesimo fuoco su Troll o Dario',
                        '2: Acceca Baldo',
                        '3: Attacca con incantesimo fuoco su Dario',
                        '4: Passa']
    print("Azioni possibili:")
    for az in azioni_possibili:
        print(az)
    scelta = input("Scegli azione (1-4): ").strip()
    if scelta == '1':
        if luigi.slot_incantesimo < 1:
            print(f"{luigi.nome} non ha abbastanza magia per incantesimo.")
            return
        print("Scegli bersaglio per palla di fuoco: (1) Troll (2) Dario")
        bersaglio = input("Scelta bersaglio: ").strip()
        if bersaglio == '1':
            luigi.incantesimo_fuoco(troll,dado)
        elif bersaglio == '2':
            luigi.incantesimo_fuoco(dario,dado)
        else:
            print("Bersaglio non valido.")
    elif scelta == '2':
        if luigi.slot_incantesimo < 3:
            print(f"{luigi.nome} non ha abbastanza magia per accecare.")
            return
        luigi.cecita(baldo, dado)
    elif scelta == '3':
        if luigi.slot_incantesimo < 1:
            print(f"{luigi.nome} non ha abbastanza magia per incantesimo.")
            return
        luigi.incantesimo_fuoco(dario, dado)
    elif scelta == '4':
        print(f"{luigi.nome} passa il turno.")
    else:
        print("Azione non valida, turno perso.")

def turno_baldo(baldo, luigi, troll, spada, dado):
    print(f"Turno di {baldo.nome}")
    print(baldo)
    print(luigi)
    print(troll)
    azioni_possibili = ['1: Attacca Troll con spada',
                        '2: Attacca Luigi con spada',
                        '3: Passa']
    print("Azioni possibili:")
    for az in azioni_possibili:
        print(az)
    scelta = input("Scegli azione (1-3): ").strip()
    if scelta == '1':
        spada.uso_spada(baldo, troll, dado)
    elif scelta == '2':
        spada.uso_spada(baldo, luigi, dado)
    elif scelta == '3':
        print(f"{baldo.nome} passa il turno.")
    else:
        print("Azione non valida, turno perso.")

def turno_troll(troll, baldo, dario, luigi, spada, dado):
    print(f"Turno di {troll.nome}")
    print(troll)
    print(baldo)
    print(dario)
    print(luigi)
    # Semplice AI: se maledetto è indebolito, altrimenti attacca Baldo o Dario con attacco fisso
    if troll.maledetto:
        danno = 3 + dadi
        bersaglio = baldo
    else:
        danno = 7 + dado
        # Scegli bersaglio: 50% Baldo / 50% Dario
        if random.random() < 0.5:
            bersaglio = baldo
        else:
            bersaglio = dario
    bersaglio.vitalita -= danno
    print(f"{troll.nome} attacca {bersaglio.nome} infliggendo {danno} danni.")

def check_fine_gioco(dario, luigi, baldo, troll):
    morti = []
    if dario.vitalita <= 0:
        morti.append(dario.nome)
    if luigi.vitalita <= 0:
        morti.append(luigi.nome)
    if baldo.vitalita <= 0:
        morti.append(baldo.nome)
    if troll.vitalita <= 0:
        morti.append(troll.nome)
    return morti

def main():
    dario = Mago("Dario", 30)
    baldo = Guerriero("Baldo", 50)
    luigi = Mago("Luigi", 30)
    troll = Troll("Troll", 50)

    bacchetta = Bacchetta_dei_fulmini()
    spada = Spada()

    print("Benvenuti alla battaglia!")
    turno = 1
    while True:
        print(f"\n--- Turno {turno} ---")
        dado = lancio_dado()
        # Turno Dario
        turno_dario(dario, baldo, luigi, troll, bacchetta, spada, dado)
        morti = check_fine_gioco(dario, luigi, baldo, troll)
        if morti:
            break
        time.sleep(1)

        # Turno Luigi
        dado2 = lancio_dado()
        turno_luigi(luigi, baldo, dario, troll, dado2)
        morti = check_fine_gioco(dario, luigi, baldo, troll)
        if morti:
            break
        time.sleep(1)

        # Turno Baldo
        dado3 = lancio_dado()
        turno_baldo(baldo, luigi, troll, spada, dado3)
        morti = check_fine_gioco(dario, luigi, baldo, troll)
        if morti:
            break
        time.sleep(1)

        # Turno Troll
        dado4 = lancio_dado()
        turno_troll(troll, baldo, dario, luigi, spada, dado4)
        morti = check_fine_gioco(dario, luigi, baldo, troll)
        if morti:
            break
        time.sleep(1)

        # Stampa stato alla fine del turno
        stampa_stato([dario, baldo, luigi, troll])
        turno += 1

    print("\n-- La battaglia è finita! --")
    if dario.vitalita <= 0:
        print(f"{dario.nome} è caduto in battaglia!")
    if luigi.vitalita <= 0:
        print(f"{luigi.nome} è caduto in battaglia!")
    if baldo.vitalita <= 0:
        print(f"{baldo.nome} è caduto in battaglia!")
    if troll.vitalita <= 0:
        print(f"{troll.nome} è caduto in battaglia!")

if __name__ == "__main__":
    main()
