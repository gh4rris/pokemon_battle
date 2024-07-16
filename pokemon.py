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
        if rng <= move.accuracy:
            foe.hp -= move.attack
            if foe.hp > 0:
                # foe.trainer.health_bar.change_hp()
                return [(f"{self.name} used {move.name}", "S-Next", lambda: foe.trainer.health_bar.change_hp())]
            foe.hp = 0
            self.fainted = True
            # foe.trainer.health_bar.change_hp()
            return [(f"{self.name} used {move.name}", "S-Next", lambda: foe.trainer.health_bar.change_hp())]
        else:
            return [(f"{self.name}'s attack missed!", "S-Next")]