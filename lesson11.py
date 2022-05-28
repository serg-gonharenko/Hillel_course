class Character:
    def __init__(self, name, health=100, rank=1, money=0):
        self.name = name
        self.__health = health
        self.rank = rank
        self.__money = money

    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health = value
        if self.__health > 100:
            self.__health = 100
        if self.__health <= 5:
            self.__health = 5

    health = property(get_health, set_health)

    def get_money(self):
        return self.__money

    def set_money(self, value):
        self.__money = value

    money = property(get_money, set_money)


class Hero(Character):

    def __init__(self, name, health, rank, money=50):
        super().__init__(name, health, rank, money)
        self.strength = self.health / 30 * self.rank

    def strength_recount(self):
        self.strength = self.health / 30 * self.rank

    def hit(self, opponent, rounds):
        fight(self, opponent, rounds)


class Wizard(Character):
    def __init__(self, *args):
        super().__init__(*args)
        self.heal_strength = self.health / 10 * self.rank

    def heal(self, patient, money_for_healing):
        if money_for_healing > patient.money:
            print(f"{patient.name} have not enough money")
            return
        else:
            patient.money = patient.money - money_for_healing
            self.money = self.money + money_for_healing
            patient.health = patient.health + self.heal_strength * money_for_healing
            print(f"{self.name} heal {patient.name} for {self.heal_strength * money_for_healing} points")


def fight(attacker, defender, rounds):
    if attacker.health <= 5:
        print(f"{attacker.name} too weak to start fighting")
        return
    if defender.health <= 5:
        print(f"{defender.name} too weak to be call for fighting")
        return
    for i in range(1, rounds):
        print(f"{attacker.name} try to hit {defender.name}")
        defender.health = defender.health - attacker.strength
        defender.strength_recount()
        if defender.health == 5:
            print(f"{attacker.name} defeat {defender.name} and receive {defender.money} coins")
            attacker.money = attacker.money + defender.money
            defender.money = 0
            return
        else:
            print(f"{attacker.name} make damage to {defender.name} - {attacker.strength} points")
        print(f"{defender.name} answer to hit {attacker.name}")
        attacker.health = attacker.health - defender.strength
        attacker.strength_recount()
        if attacker.health == 5:
            print(f"{defender.name} defeat {attacker.name} and receive {attacker.money} coins")
            defender.money = defender.money + attacker.money
            attacker.money = 0
            return
        else:
            print(f"{defender.name} make damage to {attacker.name} - {defender.strength} points")


hercules = Hero("Hercules", 100, 3, 100)
achilles = Hero("Achilles", 30, 2, 50)
merlin = Wizard("Merlin", 3)
print(f"Hercules health - {hercules.health}")
print(f"Achilles health - {achilles.health}")
hercules.hit(achilles, 5)
print(f"Hercules health - {hercules.health}")
print(f"Achilles health - {achilles.health}")
merlin.heal(achilles, 40)
print(f"Achilles health - {achilles.health}")
hercules.hit(achilles, 3)
print(f"Hercules health - {hercules.health}")
print(f"Achilles health - {achilles.health}")


