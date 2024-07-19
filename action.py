import customtkinter as ctk
import random

class Fight(ctk.CTkFrame):
    def __init__(self, frame, battle, player, opponent):
        super().__init__(frame)
        self.battle = battle
        self.player = player
        self.opponent = opponent
        self.window = frame.window
        self.attack_1 = ctk.CTkButton(self, font=("Arial", min(frame.window.width // 35, frame.window.height // 35), "bold"))
        self.attack_2 = ctk.CTkButton(self, font=("Arial", min(frame.window.width // 35, frame.window.height // 35), "bold"))
        self.attack_3 = ctk.CTkButton(self, font=("Arial", min(frame.window.width // 35, frame.window.height // 35), "bold"))
        self.attack_4 = ctk.CTkButton(self, font=("Arial", min(frame.window.width // 35, frame.window.height // 35), "bold"))
        self.configure(fg_color="transparent")
        
    def determine_turn(self, move):
        self.place_forget()
        self.battle.next_button.configure(text="Next", anchor="se", state="disabled", command=lambda: self.battle.progress_text())
        opponent_move = random.choice(self.opponent.out.moves)
        if self.player.out.speed >= self.opponent.out.speed and self.player.out.trainer.turn == False:
            self.battle.next_text = self.player.out.attack(move, self.opponent.out)
            self.battle.next_text.extend(self.opponent.out.attack(opponent_move, self.player.out))
            self.battle.next_text.append((f"What will {self.player.out.trainer.name} do?", "S-End"))
        elif self.player.out.speed < self.opponent.out.speed and self.opponent.out.trainer.turn == False:
            self.battle.next_text = self.opponent.out.attack(opponent_move, self.player.out)
            self.battle.next_text.extend(self.player.out.attack(move, self.opponent.out))
            self.battle.next_text.append((f"What will {self.player.out.trainer.name} do?", "S-End"))
        self.battle.progress_text()

    def frame_place(self):
        self.battle.switch_button_state()
        self.battle.string_var.set("")
        self.battle.next_button.configure(text="back", command=self.back, anchor="center", state="normal")
        self.attack_1.configure(text=self.player.out.moves[0].name, command=lambda: self.determine_turn(self.player.out.moves[0]))
        self.attack_2.configure(text=self.player.out.moves[1].name, command=lambda: self.determine_turn(self.player.out.moves[1]))
        self.attack_3.configure(text=self.player.out.moves[2].name, command=lambda: self.determine_turn(self.player.out.moves[2]))
        self.attack_4.configure(text=self.player.out.moves[3].name, command=lambda: self.determine_turn(self.player.out.moves[3]))
        self.attack_1.pack(expand=True, fill="both", padx=2, pady=2)
        self.attack_2.pack(expand=True, fill="both", padx=2, pady=2)
        self.attack_3.pack(expand=True, fill="both", padx=2, pady=2)
        self.attack_4.pack(expand=True, fill="both", padx=2, pady=2)
        self.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)

    def back(self):
        self.place_forget()
        self.battle.next_button.configure(text="Next", anchor="se", state="disabled")
        self.battle.next_button.configure(command=lambda: self.battle.progress_text())
        self.battle.progress_text()


class ChangePokemon(ctk.CTkFrame):
    def __init__(self, window, battle, player, opponent):
        super().__init__(window)
        self.battle = battle
        self.player = player
        self.opponent = opponent
        self.grid_columnconfigure((0, 2), weight=1, uniform="a")
        self.grid_columnconfigure(1, weight=2, uniform="a")
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")
        self.pokemon_1 = ctk.CTkButton(self, text=player.party[0].name, command=lambda: self.selected_pokemon(player.party[0]), font=("Arial", min(window.width // 35, window.height // 35), "bold"))
        self.pokemon_2 = ctk.CTkButton(self, text=player.party[1].name, command=lambda: self.selected_pokemon(player.party[1]), font=("Arial", min(window.width // 35, window.height // 35), "bold"))
        self.pokemon_3 = ctk.CTkButton(self, text=player.party[2].name, command=lambda: self.selected_pokemon(player.party[2]), font=("Arial", min(window.width // 35, window.height // 35), "bold"))
        self.pokemon_4 = ctk.CTkButton(self, text=player.party[3].name, command=lambda: self.selected_pokemon(player.party[3]), font=("Arial", min(window.width // 35, window.height // 35), "bold"))
        self.pokemon_5 = ctk.CTkButton(self, text=player.party[4].name, command=lambda: self.selected_pokemon(player.party[4]), font=("Arial", min(window.width // 35, window.height // 35), "bold"))
        self.pokemon_6 = ctk.CTkButton(self, text=player.party[5].name, command=lambda: self.selected_pokemon(player.party[5]), font=("Arial", min(window.width // 35, window.height // 35), "bold"))
        self.pokemon_buttons = [self.pokemon_1, self.pokemon_2, self.pokemon_3, self.pokemon_4, self.pokemon_5, self.pokemon_6]
        self.back = ctk.CTkButton(self, text="Back", command=lambda: self.selected_pokemon(player.out), font=("Arial", min(window.width // 35, window.height // 35), "bold"))
        self.pokemon_1.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        self.pokemon_2.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        self.pokemon_3.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        self.pokemon_4.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        self.pokemon_5.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
        self.pokemon_6.grid(row=5, column=1, sticky="nsew", padx=2, pady=2)
        self.back.grid(row=5, column=2, sticky="nsew", padx=2, pady=2)

    def selected_pokemon(self, player_pokemon):
        self.battle.switch_button_state()
        self.pack_forget()
        if player_pokemon != self.player.out:
            self.player.change_pokemon(player_pokemon)
            player_pokemon.trainer.turn = True
        else:
            opponent_previous_hp = int(self.opponent.health_bar.health_label_var.get().split("/")[0])
            if opponent_previous_hp >= 1:
                self.battle.next_text = [(f"What will {self.player.name} do?", "S-End")]
                self.battle.progress_text()
            else:
                self.opponent.no_player_change(self.battle)

    def frame_place(self):
        self.buton_states(self.player, self.back)
        self.back.configure(command=lambda: self.selected_pokemon(self.player.out))
        self.pack(expand=True, fill="both")

    def buton_states(self, player, back):
        for i, button in enumerate(self.pokemon_buttons):
            if player.party[i].fainted:
                button.configure(state="disabled")
        if player.out.fainted:
            back.configure(state="disabled")