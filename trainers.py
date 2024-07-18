from layout import PlayerHealthBar
import random

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

    def change_pokemon(self, battle):
        non_fainted_list = list(filter(lambda pokemon: not pokemon.fainted, self.party))
        pokemon_choice = random.choice(non_fainted_list)
        battle.next_text = [(f"{self.name} is about to use {pokemon_choice.name}", "S-Next"), (f"\nWill {battle.player.name} change pokemon?", "End", lambda: battle.yes_no_buttons())]
        battle.next_button.configure(state="normal")
        self.out = pokemon_choice

    def switch_health_bars(self, battle):
        previous_out = self.health_bar.name_label_var.get()
        battle.yes_button.place_forget()
        battle.no_button.place_forget()
        self.health_bar.place_forget()
        battle.next_text = [(f"{self.name} withdrew {previous_out}", "S-Next"), (f"\n{self.name} sent out {self.out.name}", "Next", lambda: self.health_bar.place_widgets()), (f"What will {battle.player.name} do?", "S-End")]
        battle.progress_text()