import customtkinter as ctk

class Fight(ctk.CTkFrame):
    def __init__(self, frame, battle, pokemon, foe):
        super().__init__(frame)
        self.battle = battle
        self.pokemon = pokemon
        self.foe = foe
        battle.switch_button_state()
        battle.string_var.set("")
        battle.next_button.configure(text="back", command=self.back, anchor="center", state="normal")
        self.configure(fg_color="transparent")
        attack_1 = ctk.CTkButton(self, text=pokemon.moves[0].name, command=lambda: self.attack(pokemon.moves[0]))
        attack_2 = ctk.CTkButton(self, text=pokemon.moves[1].name, command=lambda: self.attack(pokemon.moves[1]))
        attack_3 = ctk.CTkButton(self, text=pokemon.moves[2].name, command=lambda: self.attack(pokemon.moves[2]))
        attack_4 = ctk.CTkButton(self, text=pokemon.moves[3].name, command=lambda: self.attack(pokemon.moves[3]))
        attack_1.pack(expand=True, fill="both", padx=2, pady=2)
        attack_2.pack(expand=True, fill="both", padx=2, pady=2)
        attack_3.pack(expand=True, fill="both", padx=2, pady=2)
        attack_4.pack(expand=True, fill="both", padx=2, pady=2)
        self.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)
        

    def attack(self, move):
        self.place_forget()
        self.battle.next_text = self.pokemon.attack(move, self.foe)
        self.battle.next_button.configure(text="Next", anchor="se", state="disabled")
        self.battle.next_button.configure(command=lambda: self.battle.progress_text(self.battle.next_text))
        self.battle.window.opponent_bar.change_hp()
        print(self.foe.hp)
        self.battle.progress_text(self.battle.next_text)

    def back(self):
        self.place_forget()
        self.battle.next_button.configure(text="Next", anchor="se", state="disabled")
        self.battle.next_button.configure(command=lambda: self.battle.progress_text(self.battle.next_text))
        self.battle.progress_text(self.battle.next_text)