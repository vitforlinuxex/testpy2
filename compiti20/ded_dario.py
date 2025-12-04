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
print(protagonista)
print("Valori", protagonista.nome,protagonista.vitalita,nemico1.vitalita)
print("nemico 1", nemico1.nome, "lancia palla di fuoco" )
protagonista.palla_di_fuoco(nemico1)
print("Valori", protagonista.nome,protagonista.vitalita,nemico1.vitalita)
protagonista.palla_di_fuoco(nemico2)
print("Vitalità del troll:",nemico2.vitalita)
print(protagonista)
protagonista.maledizione(nemico2)
print("Il Troll è maledetto: ",nemico2.maledetto)
print(protagonista)
bacchetta.uso_bacchetta(protagonista2,nemico2)
bacchetta.uso_bacchetta(protagonista,nemico2)
print("Vitalita del troll:",nemico2.vitalita)
spada.uso_spada(protagonista2,nemico1)
print(nemico1)
print(getattr(protagonista2,"cecita","Non Cieco"))
nemico1.cecita(protagonista2)
print(getattr(protagonista2,"cecita","Non Cieco"))
spada.uso_spada(protagonista2,nemico1)
print(nemico1)
protagonista.cura_cecita(protagonista2)
print(getattr(protagonista2,"cecita","Non Cieco"))
protagonista.cura_cecita(protagonista2)
protagonista.cura_cecita(nemico2)
"""
