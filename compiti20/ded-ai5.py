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
- al mago Dario farà piacere se usi parte del codice qui sotto, anche se lo modifichi, tutte le cose superflue nel codice possono essere rimosse

- l'azione deve continuare fino a quando rimane un solo mago
- la funzione accecamento deve funzionare, ora fa errore
- deve essere possibile indicare i bersagli sia con il nome che con un numero, se si sbaglia a scrivere il nome l'errore viene indicato e si pot
rà scrivere il bersaglio corretto
- il valore del dado deve sempre essere mostrato
- per i maghi deve essere mostrata anche la potenza magica rimasta
- per il guerriero deve essere mostrata se è cieco in quel momento
- mostra a ogni turno il valore del dado che ogni turno deve essere tirato nuovamente, e serve per regolare le forza delle azioni

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

class Incantatore:
    pass

class Mago(Incantatore):
    def __init__(self, nome, vitalita, magia):
        self.nome = nome
        self.vitalita = vitalita
        self.magia = magia
        self.maledetto = False
        self.cecita = False

    def usa_bacchetta(self, bersaglio, dado):
        if self.magia <= 0:
            print(f"{self.nome} non ha abbastanza potere magico per usare la bacchetta.")
            return False
        print("Zzzzzott!!")
        bersaglio.subisci_danno(dado)
        self.magia -= 1
        return True

    def controincantesimo(self):
        if self.magia <= 0:
            print(f"{self.nome} non ha abbastanza potere magico per controincanto.")
            return False
        print("Ti ho fregato!")
        self.magia -= 1
        return True

    def incantesimo_acceca(self, guerriero):
        if self.magia <= 0:
            print(f"{self.nome} non ha abbastanza potere magico per lanciare l'incantesimo.")
            return False
        if not isinstance(guerriero, Guerriero):
            print("Puoi accecare solo il Guerriero.")
            return False
        if guerriero.vitalita <= 0:
            print(f"{guerriero.nome} è già fuori combattimento.")
            return False
        guerriero.cecita = True
        print(f"{self.nome} ha accecato {guerriero.nome}!")
        self.magia -= 1
        return True

    def cura_cecita(self, guerriero):
        if guerriero.cecita:
            if not self.controincantesimo():
                return False
            guerriero.cecita = False
            print(f"{self.nome} ha guarito la cecità di {guerriero.nome}.")
            return True
        else:
            print(f"{guerriero.nome} non è accecato.")
            return False

    def subisci_danno(self, danno):
        self.vitalita -= danno
        if self.vitalita < 0:
            self.vitalita = 0
        print(f"{self.nome} subisce {danno} danni ed ha ora {self.vitalita} punti vita.")

    def __str__(self):
        cecita_str = " (Accecato)" if self.cecita else ""
        return f"Mago {self.nome}: Vitalità {self.vitalita}, Magia {self.magia}{cecita_str}"

class Guerriero:
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.cecita = False
        self.maledetto = False

    def usa_spada(self, bersaglio, dado):
        danno = dado // 2 if self.cecita else dado
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} con la spada e infligge {danno} danni!")

    def subisci_danno(self, danno):
        self.vitalita -= danno
        if self.vitalita < 0:
            self.vitalita = 0
        stato_cecita = "accecato" if self.cecita else "normale"
        print(f"{self.nome} subisce {danno} danni ed ha ora {self.vitalita} punti vita. Stato attuale: {stato_cecita}")

    def __str__(self):
        cecita_str = " (Accecato)" if self.cecita else ""
        return f"Guerriero {self.nome}: Vitalità {self.vitalita}{cecita_str}"

class Troll:
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.maledetto = False

    def subisci_danno(self, danno):
        if self.maledetto:
            danno = int(danno * 1.5)
        self.vitalita -= danno
        if self.vitalita < 0:
            self.vitalita = 0
        print(f"{self.nome} subisce {danno} danni ed ha ora {self.vitalita} punti vita.")

    def __str__(self):
        stato_maledetto = " (Maledetto)" if self.maledetto else ""
        return f"Troll {self.nome}: Vitalità {self.vitalita}{stato_maledetto}"

class Bacchetta_dei_fulmini:
    def uso_bacchetta(self, utilizzatore, bersaglio, dado):
        if isinstance(utilizzatore, Mago):
            if utilizzatore.magia <= 0:
                print("Non hai abbastanza magia per usare la bacchetta.")
                return False
            print("Zzzzzott!!")
            bersaglio.subisci_danno(dado)
            utilizzatore.magia -= 1
            return True
        else:
            print("Non puoi utilizzare la bacchetta")
            return False

def seleziona_bersaglio(personaggi):
    while True:
        print("Scegli il bersaglio:")
        for i, p in enumerate(personaggi, 1):
            vit = p.vitalita if hasattr(p, 'vitalita') else "?"
            tipo = p.__class__.__name__
            extra = ""
            if isinstance(p, Mago):
                extra = f", Magia: {p.magia}"
            if isinstance(p, Guerriero) and p.cecita:
                extra += ", Accecato"
            if hasattr(p,'maledetto') and p.maledetto:
                extra += ", Maledetto"
            print(f"{i}: {p.nome} ({tipo}, Vita: {vit}{extra})")
        scelta = input("Inserisci nome o numero del bersaglio: ").strip()
        if scelta.isdigit():
            idx = int(scelta) - 1
            if 0 <= idx < len(personaggi):
                if personaggi[idx].vitalita > 0:
                    return personaggi[idx]
                else:
                    print(f"{personaggi[idx].nome} è già fuori combattimento, scegli un altro bersaglio.")
                    continue
        else:
            scelta_lower = scelta.lower()
            corrispondenze = [p for p in personaggi if p.nome.lower() == scelta_lower and p.vitalita > 0]
            if corrispondenze:
                return corrispondenze[0]
        print("Scelta non valida, riprova.")

def mostra_stato(personaggi):
    print("\nStato attuale dei personaggi:")
    for p in personaggi:
        stato = f"{p.nome} ({p.__class__.__name__}): Vitalità {p.vitalita}"
        if isinstance(p, Mago):
            stato += f", Magia {p.magia}"
        if hasattr(p,'cecita') and p.cecita:
            stato += ", Accecato"
        if hasattr(p,'maledetto') and p.maledetto:
            stato += ", Maledetto"
        print(stato)
    print()

def main():
    dario = Mago("Dario", 30, 10)
    luigi = Mago("Luigi", 30, 10)
    baldo = Guerriero("Baldo", 50)
    troll = Troll("Troll", 50)

    bacchetta = Bacchetta_dei_fulmini()

    maghi = [dario, luigi]
    alleati_dario = [dario, baldo]
    nemici_dario = [luigi, troll]
    personaggi = [dario, luigi, baldo, troll]

    turno = 1
    print("Inizio della battaglia!")
    while True:
        print(f"\n*** Turno {turno} ***")
        dado = random.randint(1, 20)
        print(f"Valore del dado per questo turno: {dado}")
        mostra_stato(personaggi)

        # Turno Dario
        if dario.vitalita > 0:
            print(f"Valore del dado per questo turno: {dado}")
            print(f"\nTurno di {dario.nome}:")
            print("1) Usa bacchetta dei fulmini")
            print("2) Controincantesimo su mago avversario (Luigi)")
            print("3) Cura la cecità di Baldo")
            print("0) Passa turno")
            scelta = input("Scegli azione: ").strip()
            if scelta == "1":
                bersagli = [p for p in nemici_dario if p.vitalita > 0]
                if not bersagli:
                    print("Nessun nemico vivo su cui usare la bacchetta.")
                else:
                    bersaglio = seleziona_bersaglio(bersagli)
                    bacchetta.uso_bacchetta(dario, bersaglio, dado)
            elif scelta == "2":
                if luigi.vitalita > 0:
                    if not dario.controincantesimo():
                        print("Non abbastanza magia per controincantesimo.")
                else:
                    print("Luigi è già fuori combattimento.")
            elif scelta == "3":
                if baldo.vitalita > 0:
                    dario.cura_cecita(baldo)
                else:
                    print("Baldo è fuori combattimento.")
            else:
                print(f"{dario.nome} passa il turno.")

        # Controllo maghi rimasti
        maghi_vivi = [m for m in maghi if m.vitalita > 0]
        if len(maghi_vivi) <= 1:
            break

        # Turno Luigi
        if luigi.vitalita > 0:
            print(f"Valore del dado per questo turno: {dado}")
            print(f"\nTurno di {luigi.nome}:")
            print("1) Incantesimo per accecare Baldo")
            print("2) Incantesimo offensivo su Dario o Baldo")
            print("0) Passa turno")
            scelta = input("Scegli azione: ").strip()
            if scelta == "1":
                if baldo.vitalita > 0:
                    luigi.incantesimo_acceca(baldo)
                else:
                    print("Baldo è fuori combattimento.")
            elif scelta == "2":
                possibili = [dario, baldo]
                possibili = [p for p in possibili if p.vitalita > 0]
                if not possibili:
                    print("Nessun bersaglio disponibile.")
                else:
                    bersaglio = seleziona_bersaglio(possibili)
                    print(f"{luigi.nome} lancia incantesimo offensivo su {bersaglio.nome}!")
                    bersaglio.subisci_danno(dado)
                    luigi.magia -= 1
                    if luigi.magia < 0:
                        luigi.magia = 0
            else:
                print(f"{luigi.nome} passa il turno.")

        maghi_vivi = [m for m in maghi if m.vitalita > 0]
        if len(maghi_vivi) <= 1:
            break

        # Turno Baldo
        if baldo.vitalita > 0:
            print(f"\nTurno di {baldo.nome}:")
            print(f"Valore del dado per questo turno: {dado}")
            bersagli = [p for p in [luigi, troll] if p.vitalita > 0]
            if not bersagli:
                print("Nessun bersaglio per Baldo.")
            else:
                bersaglio = seleziona_bersaglio(bersagli)
                baldo.usa_spada(bersaglio, dado)

        maghi_vivi = [m for m in maghi if m.vitalita > 0]
        if len(maghi_vivi) <= 1:
            break

        # Turno Troll
        if troll.vitalita > 0:
            print(f"\nTurno di {troll.nome}:")
            print(f"Valore del dado per questo turno: {dado}")
            bersagli = [p for p in [dario, luigi, baldo] if p.vitalita > 0]
            if not bersagli:
                print("Nessun bersaglio per il Troll.")
            else:
                bersaglio = seleziona_bersaglio(bersagli)
                danno = dado
                troll.subisci_danno(danno)
                print(f"{troll.nome} attacca {bersaglio.nome} e infligge {danno} danni!")
                bersaglio.subisci_danno(danno)

        maghi_vivi = [m for m in maghi if m.vitalita > 0]
        if len(maghi_vivi) <= 1:
            break

        # Dario può maledire il troll ogni 5 turni se ha magia e troll è vivo e non maledetto
        if turno % 5 == 0 and dario.magia > 0 and troll.vitalita > 0 and not troll.maledetto:
            print(f"{dario.nome} lancia una maledizione sul Troll!")
            troll.maledetto = True
            dario.magia -= 1

        turno += 1

    print("\n*** Partita terminata! ***")
    maghi_vivi = [m for m in maghi if m.vitalita > 0]
    if len(maghi_vivi) == 1:
        print(f"Il mago rimasto in vita è {maghi_vivi[0].nome}.")
    else:
        print("Nessun mago rimasto in vita. Pareggio o tutti sconfitti.")

if __name__ == "__main__":
    main()