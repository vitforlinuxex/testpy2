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
        if self.magia <=0:
            print(f"{self.nome} non ha abbastanza potere magico per usare la bacchetta.")
            return
        print("Zzzzzott!!")
        danno = dado
        bersaglio.subisci_danno(danno)
        self.magia -= 1

    def controincantesimo(self):
        if self.magia <=0:
            print(f"{self.nome} non ha abbastanza potere magico per controincanto.")
            return False
        print("Ti ho fregato!")
        self.magia -= 1
        return True

    def incantesimo(self, azione, bersaglio=None, dado=0):
        # azione: "acceca", "cura"
        if self.magia <= 0:
            print(f"{self.nome} non ha abbastanza potere magico per lanciare l'incantesimo.")
            return False

        if azione == "acceca":
            if bersaglio is None:
                print("Non è stato specificato un bersaglio da accecare.")
                return False
            if isinstance(bersaglio, Guerriero):
                bersaglio.cecita = True
                print(f"{self.nome} ha accecato {bersaglio.nome}!")
                self.magia -= 1
                return True
            else:
                print("Puoi accecare solo il Guerriero.")
                return False
        elif azione == "cura_cecita":
            if bersaglio is None:
                print("Non è stato specificato un bersaglio da curare.")
                return False
            if bersaglio.cecita:
                if self.controincantesimo():
                    bersaglio.cecita = False
                    print(f"{self.nome} ha guarito la cecità di {bersaglio.nome}.")
                    return True
                else:
                    return False
            else:
                print(f"{bersaglio.nome} non è accecato.")
                return False
        return False

    def __str__(self):
        return f"Mago {self.nome}: Vitalità {self.vitalita}, Magia {self.magia}, Cecità: {'Sì' if self.cecita else 'No'}"

class Guerriero:
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.cecita = False
        self.maledetto = False

    def usa_spada(self, bersaglio, dado):
        if self.cecita:
            danno = max(1, dado // 2)  # Danno ridotto se accecato
        else:
            danno = dado
        bersaglio.subisci_danno(danno)
        print(f"{self.nome} attacca {bersaglio.nome} con la spada e infligge {danno} danni!")

    def __str__(self):
        return f"Guerriero {self.nome}: Vitalità {self.vitalita}, Cecità: {'Sì' if self.cecita else 'No'}"

class Troll:
    def __init__(self, nome, vitalita):
        self.nome = nome
        self.vitalita = vitalita
        self.maledetto = False

    def subisci_danno(self, danno):
        if self.maledetto:
            danno = int(danno * 1.5)  # Subisce più danno se maledetto
        self.vitalita -= danno
        print(f"{self.nome} riceve {danno} danni! Vitalità ora {self.vitalita}.")

    def __str__(self):
        return f"Troll {self.nome}: Vitalità {self.vitalita}, Maledetto: {'Sì' if self.maledetto else 'No'}"

# Funzione comune per subire danni per tutti i personaggi
def subisci_danno_personaggio(self, danno):
    self.vitalita -= danno
    print(f"{self.nome} riceve {danno} danni! Vitalità ora {self.vitalita}.")

# Aggiungo metodo comune per Mago e Guerriero
Mago.subisci_danno = subisci_danno_personaggio
Guerriero.subisci_danno = subisci_danno_personaggio

# Bacchetta dei fulmini modificata per Mago Dario
class Bacchetta_dei_fulmini:
    def uso_bacchetta(self, utilizzatore, nemico, dado):
        if isinstance(utilizzatore, Mago):
            if utilizzatore.magia <= 0:
                print("Non hai abbastanza magia per usare la bacchetta.")
                return False
            print("Zzzzzott!!")
            danno = dado
            nemico.subisci_danno(danno)
            utilizzatore.magia -= 1
            return True
        else:
            print("Non puoi utilizzare la bacchetta")
            return False

# Funzione per selezionare bersaglio con gestione errori e input
def seleziona_bersaglio(personaggi):
    while True:
        print("Scegli il bersaglio:")
        for i, p in enumerate(personaggi, 1):
            print(f"{i}: {p.nome} ({p.__class__.__name__}) Vitalità: {p.vitalita}")
        scelta = input("Inserisci nome o numero del bersaglio: ").strip()
        # Controllo se è numero valido
        if scelta.isdigit():
            idx = int(scelta) - 1
            if 0 <= idx < len(personaggi):
                bersaglio = personaggi[idx]
                if bersaglio.vitalita <= 0:
                    print(f"{bersaglio.nome} è già fuori combattimento, scegli un altro bersaglio.")
                    continue
                return bersaglio
        else:
            # Cerca per nome in minuscolo (gestione case insensitive)
            scelta_norm = scelta.lower()
            corrispondenze = [p for p in personaggi if p.nome.lower() == scelta_norm and p.vitalita > 0]
            if corrispondenze:
                return corrispondenze[0]
        print("Scelta non valida, riprova.")

def mostra_stato(personaggi):
    print("\nStato attuale dei personaggi:")
    for p in personaggi:
        stato = f"{p.nome} ({p.__class__.__name__}): Vitalità {p.vitalita}"
        if isinstance(p, Mago):
            stato += f", Magia {p.magia}"
        if hasattr(p, 'cecita') and p.cecita:
            stato += ", Accecato"
        if hasattr(p, 'maledetto') and p.maledetto:
            stato += ", Maledetto"
        print(stato)
    print()

def round_di_gioco():
    # Inizializzazione personaggi
    dario = Mago("Dario", 30, 10)
    luigi = Mago("Luigi", 30, 10)
    baldo = Guerriero("Baldo", 50)
    troll = Troll("Troll", 50)
    bacchetta = Bacchetta_dei_fulmini()
    spada = None  # il guerriero usa il suo metodo per attaccare

    maghi = [dario, luigi]
    alleati_dario = [dario, baldo]
    nemici_dario = [luigi, troll]

    personaggi = [dario, luigi, baldo, troll]

    turno = 1
    while True:
        print(f"\n--- Turno {turno} ---")

        dado = random.randint(1, 20)
        print(f"[Dado estratto per gli effetti questa partita: {dado}]")

        # Mostra stato
        mostra_stato(personaggi)

        # Azioni maghi alla fine della riga
        # Primo: Dario (mago)
        if dario.vitalita > 0:
            print(f"\nTurno di {dario.nome}:")
            print("Azioni disponibili:")
            print("1: Usa bacchetta dei fulmini (costruito per Dario) contro nemico")
            print("2: Controincantesimo su mago nemico")
            print("3: Cura cecità su Baldo (se accecato)")
            print("0: Passa turno")
            scelta = input("Scegli azione: ").strip()
            if scelta == "1":
                bersagli_possibili = [nem for nem in nemici_dario if nem.vitalita > 0]
                if not bersagli_possibili:
                    print("Non ci sono nemici validi per la bacchetta.")
                else:
                    bersaglio = seleziona_bersaglio(bersagli_possibili)
                    bacchetta.uso_bacchetta(dario, bersaglio, dado)
            elif scelta == "2":
                # Dario fa controincantesimo a uno dei maghi nemici se ha magia
                if luigi.vitalita > 0:
                    riuscito = dario.controincantesimo()
                    if riuscito:
                        # il controincantesimo impedisce a luigi di fare incantesimi questo turno? 
                        # per semplificare riduciamo magia a 0 per forzare skip del turno incantesimi
                        luigi.magia = max(0, luigi.magia - 2)
                    else:
                        print("Controincantesimo fallito per mancanza di magia.")
                else:
                    print("Luigi è già fuori combattimento.")
            elif scelta == "3":
                if baldo.vitalita > 0:
                    if baldo.cecita:
                        dario.incantesimo("cura_cecita", baldo)
                    else:
                        print("Baldo non è accecato.")
                else:
                    print("Baldo è fuori combattimento.")
            else:
                print(f"{dario.nome} passa il turno.")

        # Leggo se Dario o Luigi sono vivi per valutare la fine
        maghi_vivi = [mago for mago in maghi if mago.vitalita > 0]
        if len(maghi_vivi) <= 1:
            break

        # Secondo: Luigi (mago)
        if luigi.vitalita > 0:
            print(f"\nTurno di {luigi.nome}:")
            print("Azioni disponibili:")
            print("1: Incantesimo di accecamento su Baldo")
            print("2: Attacca con incantesimo base il nemico (Dario o alleati?)")
            print("0: Passa turno")
            scelta = input("Scegli azione: ").strip()
            if scelta == "1":
                if baldo.vitalita > 0:
                    riuscito = luigi.incantesimo("acceca", baldo)
                    if not riuscito:
                        print("Incantesimo fallito.")
                else:
                    print("Baldo è fuori combattimento.")
            elif scelta == "2":
                # Luigi usa incantesimo offensivo, danneggia Dario o Baldo
                possibili_bersagli = [dario, baldo]
                possibili_bersagli = [p for p in possibili_bersagli if p.vitalita > 0]
                if not possibili_bersagli:
                    print("Nessun bersaglio disponibile per l'attacco.")
                else:
                    bersaglio = seleziona_bersaglio(possibili_bersagli)
                    danno = dado
                    bersaglio.subisci_danno(danno)
                    luigi.magia -= 1
                    print(f"{luigi.nome} usa incantesimo su {bersaglio.nome} e infligge {danno} danni!")
            else:
                print(f"{luigi.nome} passa il turno.")

        maghi_vivi = [mago for mago in maghi if mago.vitalita > 0]
        if len(maghi_vivi) <= 1:
            break

        # Terzo: Baldo (guerriero)
        if baldo.vitalita > 0:
            print(f"\nTurno di {baldo.nome}:")
            # Sceglie tra troll e Luigi
            bersagli_possibili = [luigi, troll]
            bersagli_possibili = [p for p in bersagli_possibili if p.vitalita > 0]
            if not bersagli_possibili:
                print("Nessun bersaglio per Baldo.")
            else:
                bersaglio = seleziona_bersaglio(bersagli_possibili)
                baldo.usa_spada(bersaglio, dado)

        maghi_vivi = [mago for mago in maghi if mago.vitalita > 0]
        if len(maghi_vivi) <= 1:
            break

        # Quarto: Troll
        if troll.vitalita > 0:
            print(f"\nTurno di {troll.nome}:")
            # Attacca uno degli umani
            bersagli_possibili = [dario, baldo, luigi]
            bersagli_possibili = [p for p in bersagli_possibili if p.vitalita > 0]
            if not bersagli_possibili:
                print("Nessun bersaglio per il Troll.")
            else:
                bersaglio = seleziona_bersaglio(bersagli_possibili)
                danno = dado
                troll.subisci_danno = subisci_danno_personaggio.__get__(troll)  # usa metodo comune se manca
                bersaglio.subisci_danno(danno)
                print(f"{troll.nome} attacca {bersaglio.nome} e infligge {danno} danni!")

        maghi_vivi = [mago for mago in maghi if mago.vitalita > 0]
        if len(maghi_vivi) <= 1:
            break

        # Aggiungiamo verifica se troll è maledetto, con possibilità che Dario maledice il troll ogni tot turni
        if not troll.maledetto and turno % 5 == 0 and dario.magia > 0 and troll.vitalita > 0:
            print(f"{dario.nome} lancia maledizione contro il Troll!")
            troll.maledetto = True
            dario.magia -= 1

        turno += 1

    # Fine gioco
    print("\n--- Partita terminata! ---")
    maghi_vivi = [mago for mago in maghi if mago.vitalita > 0]
    if len(maghi_vivi) == 1:
        vincitore = maghi_vivi[0]
        print(f"Il mago rimasto in vita è {vincitore.nome}, vincitore dello scontro!")
    else:
        print("Nessun mago rimasto in vita, pareggio o tutti sconfitti.")

if __name__ == "__main__":
    round_di_gioco()
