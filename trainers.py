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

    def yes_player_change(self, battle):
        battle.change_pokemon_button.cget("command")()
        battle.yes_button.place_forget()
        battle.no_button.place_forget()
        battle.switch_button_state()

    def no_player_change(self, battle):
        battle.yes_button.place_forget()
        battle.no_button.place_forget()
        self.health_bar.place_forget()
        battle.next_text = self.set_text()
        battle.progress_text()

    def set_text(self):
        previous_out = self.health_bar.name_label_var.get()
        text = [(f"{self.name} withdrew {previous_out}", "S-Next"), (f"\n{self.name} sent out {self.out.name}", "Next", lambda: self.health_bar.place_widgets()), (f"What will {self.battle.player.name} do?", "S-End")]
        if not self.battle.player.turn:
            return text
        text[0] += (lambda: self.health_bar.place_forget(),)
        return text