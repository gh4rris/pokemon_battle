import random

class Pokemon():
    def __init__(self, name, base_health, base_speed, lvl, moves, trainer):
        self.name = name
        self.max_hp = int(round(base_health * lvl))
        self.hp = self.max_hp
        self.speed = int(round(base_speed * lvl))
        self.lvl = lvl
        self.moves = moves
        self.fainted = False
        self.trainer = trainer

    def attack(self, move, foe):
        rng = random.randint(1, 100)
        text = [(f"{self.name} used {move.name}", "S-Next")]
        self.trainer.turn = True
        if rng <= move.accuracy:
            text[0] = text[0] + (lambda: foe.trainer.health_bar.change_hp(),)
            foe.hp -= move.attack
            if foe.hp > 0:
                return text
            foe.hp = 0
            foe.fainted = True
            text.append((f"\n{foe.name} fainted!", "End"))
            return text
        else:
            text.append((f"\n{self.name}'s attack missed!", "Next"))
            return text