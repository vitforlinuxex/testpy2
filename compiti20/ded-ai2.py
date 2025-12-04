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
- l'azione deve continuare fino a quando rimane un solo mago

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
        danno_base = 5 if getattr(utilizzatore, "cecita", "Non Cieco") == "Cieco" else 10
        danno = danno_base + potenza
        nemico.vitalita -= danno
        print(f"{utilizzatore.nome} usa la spada e infligge {danno} danni a {nemico.nome}.")

class Bacchetta_dei_fulmini:
    def uso_bacchetta(self, utilizzatore, nemico, potenza):
        if isinstance(utilizzatore, Incantatore) and utilizzatore.slot_incantesimo >= 2:
            print("Zzzzzott!!")
            danno = 15 + potenza
            nemico.vitalita -= danno
            utilizzatore.slot_incantesimo -= 2
            print(f"{utilizzatore.nome} colpisce {nemico.nome} con la bacchetta dei fulmini infliggendo {danno} danni.")
        else:
            print(f"{utilizzatore.nome} non può usare la bacchetta (magia insufficiente o non incantatore).")

class Guerriero:
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.maledetto = False
        # La cecità è solo un attributo di singola istanza
        self.cecita = False

    def __str__(self):
        stato_cecita = "Cieco" if self.cecita else "Normale"
        stato_maledizione = "Maledetto" if self.maledetto else "Non maledetto"
        return f"*-----------*\nGuerriero {self.nome}:\nVitalità: {self.vitalita}\nStato cecità: {stato_cecita}\nStato maledizione: {stato_maledizione}\n*-----------*"

class Mago(Incantatore):
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.slot_incantesimo = 10
        self.maledetto = False
        self.cecita = False  # aggiungo anche per maghi così potenziale cecità

    def palla_di_fuoco(self, other, potenza):
        if self.slot_incantesimo > 0:
            danno = random.randint(5, 40) + potenza
            # Se l'altro non può fare controincantesimo
            if not hasattr(other, "controincantesimo") or other.slot_incantesimo <= 0:
                other.vitalita -= danno
                print(f"{self.nome} lancia palla di fuoco su {other.nome} e infligge {danno} danni.")
            else:
                other.controincantesimo()
            self.slot_incantesimo -= 1
        else:
            print(f"{self.nome} non ha magia sufficiente per lanciare la palla di fuoco.")

    def controincantesimo(self):
        print("Ti ho fregato!")
        if self.slot_incantesimo > 0:
            self.slot_incantesimo -= 1

    def cura_ferite(self, other, potenza):
        if self.slot_incantesimo >= 2:
            cura = 10 + potenza
            other.vitalita += cura
            print(f"{self.nome} cura {other.nome} di {cura} punti.")
            self.slot_incantesimo -= 2
        else:
            print(f"{self.nome} non ha magia sufficiente per curare.")

    def maledizione(self, other, potenza):
        if self.slot_incantesimo >= 2:
            other.maledetto = True
            danno = 5 + potenza
            other.vitalita -= danno
            print(f"{self.nome} scaglia una maledizione su {other.nome} causando {danno} danni e maledizione.")
            self.slot_incantesimo -= 2
        else:
            print(f"{self.nome} non ha magia sufficiente per maledire.")

    def cecita(self, other, potenza):
        if self.slot_incantesimo >= 3:
            if hasattr(other, "cecita"):
                other.cecita = True
                print(f"{self.nome} acceca {other.nome}!")
                self.slot_incantesimo -= 3
            else:
                print(f"{other.nome} non può essere accecato.")
        else:
            print(f"{self.nome} non ha magia sufficiente per accecare.")

    def cura_cecita(self, other):
        if self.slot_incantesimo >= 2:
            if hasattr(other, "cecita") and other.cecita:
                other.cecita = False
                print(f"{self.nome} rimuove la cecità da {other.nome}.")
                self.slot_incantesimo -= 2
            else:
                print(f"{other.nome} non è accecato.")
        else:
            print(f"{self.nome} non ha magia sufficiente per curare la cecità.")

    def __str__(self):
        stato_cecita = "Cieco" if self.cecita else "Normale"
        stato_maledizione = "Maledetto" if self.maledetto else "Non maledetto"
        return (f"*-----------*\nScheda di {self.nome}:\nVitalità: {self.vitalita}\nMagia: {self.slot_incantesimo}\n"
                f"Stato cecità: {stato_cecita}\nStato maledizione: {stato_maledizione}\n*-----------*")

class Troll:
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.maledetto = False

    def __str__(self):
        stato_maledizione = "Maledetto" if self.maledetto else "Non maledetto"
        return f"*-----------*\nTroll {self.nome}:\nVitalità: {self.vitalita}\nStato maledizione: {stato_maledizione}\n*-----------*"

def lancio_dado():
    dado = random.randint(1,6)
    print(f"\nDado lanciato: {dado}\n")
    return dado

def azione_dario(dario, baldo, luigi, troll, bacchetta, spada, dado):
    print(f"Turno di {dario.nome}:")
    print(dario)
    print(baldo)
    print(luigi)
    print(troll)
    print("Scegli azione:")
    print("1: Usa bacchetta dei fulmini su nemico (Luigi o Troll)")
    print("2: Controincantesimo su Luigi")
    print("3: Cura ferite di Baldo")
    print("4: Guarisci cecità di Baldo")
    print("5: Attacca Troll con la spada")
    scelta = input("Azione (1-5): ").strip()

    if scelta == '1':
        if dario.slot_incantesimo < 2:
            print(f"{dario.nome} non ha magia sufficiente per usare la bacchetta.")
            return
        bersaglio = input("Bersaglio (luigi/troll): ").strip().lower()
        if bersaglio == 'luigi':
            bacchetta.uso_bacchetta(dario, luigi, dado)
        elif bersaglio == 'troll':
            bacchetta.uso_bacchetta(dario, troll, dado)
        else:
            print("Bersaglio non valido.")
    elif scelta == '2':
        if dario.slot_incantesimo <1:
            print(f"{dario.nome} non ha magia sufficiente per fare controincantesimo.")
            return
        print(f"{dario.nome} fa controincantesimo a Luigi.")
        luigi.controincantesimo()
    elif scelta == '3':
        dario.cura_ferite(baldo, dado)
    elif scelta == '4':
        dario.cura_cecita(baldo)
    elif scelta == '5':
        spada.uso_spada(baldo, troll, dado)
    else:
        print("Azione non valida.")

def azione_luigi(luigi, baldo, dario, troll, dado):
    print(f"Turno di {luigi.nome}:")
    print(luigi)
    print(baldo)
    print(dario)
    print(troll)
    print("Scegli azione:")
    print("1: Lancia palla di fuoco su Dario o Troll")
    print("2: Acceca Baldo")
    print("3: Passa il turno")
    scelta = input("Azione (1-3): ").strip()

    if scelta == '1':
        if luigi.slot_incantesimo < 1:
            print(f"{luigi.nome} non ha magia sufficiente per lanciare la palla di fuoco.")
            return
        bersaglio = input("Bersaglio (dario/troll): ").strip().lower()
        if bersaglio == 'dario':
            luigi.palla_di_fuoco(dario, dado)
        elif bersaglio == 'troll':
            luigi.palla_di_fuoco(troll, dado)
        else:
            print("Bersaglio non valido.")
    elif scelta == '2':
        if luigi.slot_incantesimo < 3:
            print(f"{luigi.nome} non ha magia sufficiente per accecare.")
            return
        luigi.cecita(baldo, dado)
    elif scelta == '3':
        print(f"{luigi.nome} passa il turno.")
    else:
        print("Azione non valida.")

def azione_baldo(baldo, luigi, troll, spada, dado):
    print(f"Turno di {baldo.nome}:")
    print(baldo)
    print(luigi)
    print(troll)
    print("Scegli azione:")
    print("1: Attacca Troll")
    print("2: Attacca Luigi")
    print("3: Passa il turno")
    scelta = input("Azione (1-3): ").strip()
    if scelta == '1':
        spada.uso_spada(baldo, troll, dado)
    elif scelta == '2':
        spada.uso_spada(baldo, luigi, dado)
    elif scelta == '3':
        print(f"{baldo.nome} passa il turno.")
    else:
        print("Azione non valida.")

def azione_troll(troll, baldo, dario, luigi, dado):
    print(f"Turno di {troll.nome}:")
    print(troll)
    print(baldo)
    print(dario)
    print(luigi)
    # Decide a chi attaccare: Baldo (amico Dario) o Dario o Luigi
    # Troll attacca il guerriero se non maledetto, altrimenti sceglie uno dei maghi
    if troll.maledetto:
        danno = max(1, 7 - 3)
    else:
        danno = 7
    # Sceglie il bersaglio
    bersaglio = random.choice([baldo, dario, luigi])
    bersaglio.vitalita -= danno
    print(f"{troll.nome} attacca {bersaglio.nome} infliggendo {danno} danni.")

def conta_maghi_vivi(maghi):
    return sum(1 for m in maghi if m.vitalita > 0)

def stampa_stato(personaggi):
    for p in personaggi:
        print(p)

def main():
    dario = Mago("Dario", 30)
    baldo = Guerriero("Baldo", 50)
    luigi = Mago("Luigi", 30)
    troll = Troll("Troll", 50)

    bacchetta = Bacchetta_dei_fulmini()
    spada = Spada()

    print("Benvenuti al gioco di battaglia in stile Dungeons and Dragons!\n")

    turno = 1
    while True:
        print(f"\n--- Turno {turno} ---")
        dado = lancio_dado()

        if dario.vitalita > 0:
            azione_dario(dario, baldo, luigi, troll, bacchetta, spada, dado)
        else:
            print(f"{dario.nome} è fuori combattimento!")

        if luigi.vitalita > 0:
            dado = lancio_dado()
            azione_luigi(luigi, baldo, dario, troll, dado)
        else:
            print(f"{luigi.nome} è fuori combattimento!")

        if baldo.vitalita > 0:
            dado = lancio_dado()
            azione_baldo(baldo, luigi, troll, spada, dado)
        else:
            print(f"{baldo.nome} è fuori combattimento!")

        if troll.vitalita > 0:
            dado = lancio_dado()
            azione_troll(troll, baldo, dario, luigi, dado)
        else:
            print(f"{troll.nome} è fuori combattimento!")

        stampa_stato([dario, baldo, luigi, troll])

        maghi_vivi = conta_maghi_vivi([dario, luigi])
        if maghi_vivi <= 1:
            print("\nIl combattimento termina: è rimasto un solo mago o nessuno.")
            break

        # Ritardo per evitare troppe stampe consecutive
        time.sleep(1)
        turno += 1

    print("\n--- Risultati finali ---")
    stampa_stato([dario, baldo, luigi, troll])
    if dario.vitalita > 0 and luigi.vitalita <= 0:
        print("Dario è l'unico mago rimasto!")
    elif luigi.vitalita > 0 and dario.vitalita <= 0:
        print("Luigi è l'unico mago rimasto!")
    elif dario.vitalita <= 0 and luigi.vitalita <= 0:
        print("Nessun mago è rimasto in piedi!")

if __name__ == "__main__":
    main()
