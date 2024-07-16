from layout import PlayerHealthBar

class Player():
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.out = None
        self.battle = None
        self.health_bar = None
        self.turn = False

    def change_pokemon(self, pokemon):
        self.health_bar.place_forget()
        self.battle.next_text = [(f"{self.out.name} come back!", "S-Next"), (f"Go {pokemon.name}!", "S-Next", lambda: self.health_bar.place_widgets()), (f"What will {self.name} do?", "S-End")]
        self.battle.progress_text()
        self.out = pokemon
 


class Opponent():
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.out = None
        self.battle = None
        self.health_bar = None
        self.turn = False