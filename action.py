import customtkinter as ctk
import random

class Fight(ctk.CTkFrame):
    def __init__(self, parent, battle, player_pokemon, opponent_pokemon):
        super().__init__(parent)
        self.battle = battle
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon
        battle.switch_button_state()
        battle.string_var.set("")
        battle.next_button.configure(text="back", command=self.back, anchor="center", state="normal")
        self.configure(fg_color="transparent")
        attack_1 = ctk.CTkButton(self, text=player_pokemon.moves[0].name, command=lambda: self.determine_turn(player_pokemon.moves[0]))
        attack_2 = ctk.CTkButton(self, text=player_pokemon.moves[1].name, command=lambda: self.determine_turn(player_pokemon.moves[1]))
        attack_3 = ctk.CTkButton(self, text=player_pokemon.moves[2].name, command=lambda: self.determine_turn(player_pokemon.moves[2]))
        attack_4 = ctk.CTkButton(self, text=player_pokemon.moves[3].name, command=lambda: self.determine_turn(player_pokemon.moves[3]))
        attack_1.pack(expand=True, fill="both", padx=2, pady=2)
        attack_2.pack(expand=True, fill="both", padx=2, pady=2)
        attack_3.pack(expand=True, fill="both", padx=2, pady=2)
        attack_4.pack(expand=True, fill="both", padx=2, pady=2)
        self.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)
        
    def determine_turn(self, move):
        self.place_forget()
        self.battle.next_button.configure(text="Next", anchor="se", state="disabled", command=lambda: self.battle.progress_text())
        opponent_move = random.choice(self.opponent_pokemon.moves)
        if self.player_pokemon.speed >= self.opponent_pokemon.speed and self.player_pokemon.trainer.turn == False:
            self.battle.next_text = self.player_pokemon.attack(move, self.opponent_pokemon)
            self.battle.next_text.extend(self.opponent_pokemon.attack(opponent_move, self.player_pokemon))
            self.battle.next_text.append((f"What will {self.player_pokemon.trainer.name} do?", "S-End"))
        elif self.player_pokemon.speed < self.opponent_pokemon.speed and self.opponent_pokemon.trainer.turn == False:
            self.battle.next_text = self.opponent_pokemon.attack(opponent_move, self.player_pokemon)
            self.battle.next_text.extend(self.player_pokemon.attack(move, self.opponent_pokemon))
            self.battle.next_text.append((f"What will {self.player_pokemon.trainer.name} do?", "S-End"))
        self.battle.progress_text()

    def back(self):
        self.place_forget()
        self.battle.next_button.configure(text="Next", anchor="se", state="disabled")
        self.battle.next_button.configure(command=lambda: self.battle.progress_text(self.battle.next_text))
        self.battle.progress_text()


class ChangePokemon(ctk.CTkFrame):
    def __init__(self, parent, battle, player):
        super().__init__(parent)
        self.battle = battle
        self.player = player
        self.pack(expand=True, fill="both")
        self.grid_columnconfigure((0, 2), weight=1, uniform="a")
        self.grid_columnconfigure(1, weight=2, uniform="a")
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")
        pokemon_1 = ctk.CTkButton(self, text=player.party[0].name, command=lambda: self.selected_pokemon(player.party[0]))
        pokemon_2 = ctk.CTkButton(self, text=player.party[1].name, command=lambda: self.selected_pokemon(player.party[1]))
        self.pokemon_buttons = [pokemon_1, pokemon_2]
        back = ctk.CTkButton(self, text="Back", command=lambda: self.selected_pokemon(player.out))
        self.buton_states(player, back)
        pokemon_1.grid(row=0, column=1, sticky="nsew")
        pokemon_2.grid(row=1, column=1, sticky="nsew")
        back.grid(row=5, column=2, sticky="nsew")

    def selected_pokemon(self, player_pokemon):
        self.battle.switch_button_state()
        self.pack_forget()
        if player_pokemon != self.player.out:
            self.player.change_pokemon(player_pokemon)
            player_pokemon.trainer.turn = True
        else:
            self.battle.next_text = [(f"What will {self.player.name} do?", "S-End")]
            self.battle.progress_text()

    def buton_states(self, player, back):
        for i, button in enumerate(self.pokemon_buttons):
            if player.party[i].fainted:
                button.configure(state="disabled")
        if player.out.fainted:
            back.configure(state="disabled")