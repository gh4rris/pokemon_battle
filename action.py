import customtkinter as ctk
import random

class Fight(ctk.CTkFrame):
    def __init__(self, frame, battle, player_pokemon, opponent_pokemon):
        super().__init__(frame)
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
        

    def attack(self, pokemon, move, foe):
        self.place_forget()
        self.battle.next_button.configure(text="Next", anchor="se", state="disabled", command=lambda: self.battle.progress_text())
        self.battle.next_text = pokemon.attack(move, foe)
        pokemon.trainer.turn = True
        self.battle.progress_text()
        # self.battle.next_text = foe.attack(foe_move, pokemon)
        
        # self.battle.next_text = self.opponent_pokemon.attack(opponent_move, self.pokemon)
        # self.opponent_pokemon.trainer.turn = True
        # self.battle.progress_text()

    def determine_turn(self, move):
        opponent_move = random.choice(self.opponent_pokemon.moves)
        if self.player_pokemon.speed >= self.opponent_pokemon.speed and self.player_pokemon.trainer.turn == False:
            self.attack(self.player_pokemon, move, self.opponent_pokemon)
            self.player_pokemon.trainer.turn = True
        elif self.player_pokemon.speed < self.opponent_pokemon.speed and self.opponent_pokemon.trainer.turn == False:
            self.attack(self.opponent_pokemon, opponent_move, self.player_pokemon)
            self.opponent_pokemon.trainer.turn = True
        elif self.player_pokemon.trainer.turn == False:
            self.attack(self.player_pokemon, move, self.opponent_pokemon)
            self.player_pokemon.trainer.turn = True
        else:
            self.attack(self.opponent_pokemon, opponent_move, self.player_pokemon)
            self.opponent_pokemon.trainer.turn = True

    def back(self):
        self.place_forget()
        self.battle.next_button.configure(text="Next", anchor="se", state="disabled")
        self.battle.next_button.configure(command=lambda: self.battle.progress_text(self.battle.next_text))
        self.battle.progress_text()