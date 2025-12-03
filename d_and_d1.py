import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} riceve {amount} danni. HP rimanenti: {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} è stato sconfitto!")

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacca {other.name} causando {damage} danni.")
        other.take_damage(damage)

class Mage(Character):
    def __init__(self, name, hp=30, attack_power=10, mana=20):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def cast_spell(self, other):
        if self.mana < 5:
            print(f"{self.name} non ha abbastanza mana per lanciare una magia.")
            return
        self.mana -= 5
        damage = random.randint(5, self.attack_power + 5)
        print(f"{self.name} lancia una magia su {other.name} causando {damage} danni. Mana rimasto: {self.mana}")
        other.take_damage(damage)

    def attack(self, other):
        # usa hasattr per decidere se può lanciare un incantesimo o attaccare fisicamente
        if hasattr(self, 'cast_spell'):
            self.cast_spell(other)
        else:
            super().attack(other)

class Troll(Character):
    def __init__(self, name="Troll", hp=50, attack_power=12):
        super().__init__(name, hp, attack_power)

    def attack(self, other):
        # Attacco fisico potente
        damage = random.randint(3, self.attack_power)
        print(f"{self.name} colpisce con forza {other.name} causando {damage} danni.")
        other.take_damage(damage)

def game():
    dario = Mage("Dario")
    luigi = Mage("Luigi")
    troll = Troll()

    characters = [dario, luigi, troll]

    turn = 0
    while sum(c.is_alive() for c in characters if isinstance(c, Mage)) > 0 and troll.is_alive():
        attacker = characters[turn % 3]
        if attacker.is_alive():
            if isinstance(attacker, Mage):
                target = troll
            else:
                # Il troll sceglie un mago vivo casuale come bersaglio
                targets = [c for c in characters if isinstance(c, Mage) and c.is_alive()]
                if targets:
                    target = random.choice(targets)
                else:
                    break

            attacker.attack(target)
        turn += 1
        print("---")

    if troll.is_alive():
        print("Il troll ha vinto!")
    else:
        print("I maghi hanno sconfitto il troll!")

if __name__ == "__main__":
    game()