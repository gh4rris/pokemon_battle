import random

class Pokemon():
    def __init__(self, name, base_health, lvl, moves):
        self.name = name
        self.max_hp = round(base_health * lvl)
        self.hp = self.max_hp
        self.lvl = lvl
        self.moves = moves

    def attack(self, move, foe):
        rng = random.randint(1, 100)
        if rng <= move.accuracy:
            foe.hp -= move.attack
            return f"{self.name} used {move.name}"
        else:
            return f"{self.name}'s attack missed!"