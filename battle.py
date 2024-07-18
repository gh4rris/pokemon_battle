import customtkinter as ctk
import random
import time
from action import Fight, ChangePokemon

class Battle(ctk.CTkLabel):
    def __init__(self, frame, window, player, opponent):
        super().__init__(frame)
        self.frame = frame
        self.window = window
        self.string_var = ctk.StringVar()
        self.current_font = ("Arial", min(self.window.width // 20, self.window.height // 20), "bold")
        self.configure(textvariable=self.string_var, anchor="nw", font=self.current_font, justify="left")
        self.window.bind("<Configure>", self.update_font_size)
        self.grid(row=0, column=0, sticky="nsew", rowspan=2, padx=25, pady=25)
        self.player = player
        self.opponent = opponent
        player.battle = self
        opponent.battle = self

        # Widgets
        self.fight_button = ctk.CTkButton(self.frame, text="Fight", state="disabled", command=lambda: Fight(self.frame, self, player.out, opponent.out))
        self.change_pokemon_button = ctk.CTkButton(self.frame, text="Change Pokemon", state="disabled", command=lambda: ChangePokemon(self.window, self, player, opponent))
        self.item_button = ctk.CTkButton(self.frame, text="Item", state="disabled")
        self.run_button = ctk.CTkButton(self.frame, text="Run", state="disabled")
        self.next_text = None
        self.next_button = ctk.CTkButton(frame, text="Next", command=self.progress_text, anchor="se", state="disabled")
        self.yes_button = ctk.CTkButton(self.frame, text="Yes", command=lambda: opponent.yes_player_change(self))
        self.no_button = ctk.CTkButton(self.frame, text="No", command=lambda: opponent.no_player_change(self))
        
        self.fight_button.grid(row=0, column=1, sticky="nsew", padx=3, pady=3)
        self.change_pokemon_button.grid(row=0, column=2, sticky="nsew", padx=3, pady=3)
        self.item_button.grid(row=1, column=1, sticky="nsew", padx=3, pady=3)
        self.run_button.grid(row=1, column=2, sticky="nsew", padx=3, pady=3)
        self.next_button.place(relx=0.6, rely=1, relwidth=0.2, relheight=0.3, anchor="se")

    def oppening_battle(self, player, opponent):
        self.next_text = [(f"Champion {opponent.name} wants to battle!", "Next")]
        self.progress_text()
        self.next_text = [(f"\n{opponent.name} sent out {opponent.party[0].name}", "Next", lambda: self.send_pokemon_out(opponent, opponent.party[0])), 
                          (f"\nGo {player.party[0].name}!", "Next", lambda: self.send_pokemon_out(player, player.party[0])), 
                          (f"What will {player.name} do?", "S-End")]

    def send_pokemon_out(self, trainer, pokemon):
        trainer.out = pokemon
        trainer.health_bar.place_widgets()

    def progress_text(self):
        # print(f"player: {self.player.turn}, opponent: {self.opponent.turn}")
        self.next_button.configure(state="disabled")
        if self.player.out !=None and self.player.out.fainted and len(self.next_text) == 3:
            self.change_pokemon_button.configure(state="disabled")
        line = self.next_text[0]
        if line[1].startswith("S"):
            self.grid_forget()
            self.string_var.set("")
            self.grid(row=0, column=0, sticky="nsew", rowspan=2, padx=25, pady=25)
        self.animate_text(line[0])
        if len(line) == 3:
            line[2]()
        if len(self.next_text) > 1:
            self.next_text = self.next_text[1:]
        if line[1].endswith("Next"):
            self.next_button.configure(state="normal")
        else:   
            self.switch_button_state()
        if self.player.out != None:
            self.turn_conditions()

    def turn_conditions(self):
        if self.player.turn == True and self.opponent.turn == True and len(self.next_text) == 1 and not self.player.out.fainted:
            self.player.turn = False
            self.opponent.turn = False
        elif self.player.turn == True and self.opponent.turn == False and len(self.next_text) == 1:
            previous_hp = int(self.opponent.health_bar.health_label_var.get().split("/")[0])
            if previous_hp >= 1:
                opponent_move = random.choice(self.opponent.out.moves)
                self.next_text = self.opponent.out.attack(opponent_move, self.player.out) + [(f"What will {self.player.name} do?", "S-End")]
            else:
                self.next_text = self.opponent.set_text()
                self.player.turn = False

    def animate_text(self, line):
        current_text = self.string_var.get()
        for i in line:
            self.string_var.set(current_text + i)
            current_text = self.string_var.get()
            self.frame.update()
            time.sleep(0.02)

    def switch_button_state(self):
        buttons = [self.fight_button, self.change_pokemon_button, self.item_button,self.run_button]
        player_not_fainted = list(filter(lambda pokemon: not pokemon.fainted, self.player.party))
        opponent_not_fainted = list(filter(lambda pokemon: not pokemon.fainted, self.opponent.party))
        if len(player_not_fainted) == 0:
            if self.next_text[0][1] == "S-End":
                self.end_game(False)
            else:
                self.next_button.configure(state="disabled")
        elif len(opponent_not_fainted) == 0:
            if self.next_text[0][1].startswith("S"):
                self.end_game(True)
            else:
                self.next_button.configure(state="disabled")
        else:
            if self.player.out.fainted and len(self.next_text) <= 3:
                for button in buttons:
                    button.configure(state="disabled")
                self.change_pokemon_button.configure(state="normal")
            elif self.opponent.out.fainted:
                self.opponent.change_pokemon(self)
            else:
                for button in buttons:
                    if button.cget("state") == "normal":
                        button.configure(state="disabled")
                    else:
                        button.configure(state="normal")

    def yes_no_buttons(self):
        self.switch_button_state()
        self.yes_button.place(relx=0.01, rely=0.95, relwidth=0.18, relheight=0.25, anchor="sw")
        self.no_button.place(relx=0.21, rely=0.95, relwidth=0.18, relheight=0.25, anchor="sw")

    def end_game(self, player_win):
        if player_win:
            self.next_text = [(f"{self.player.name} defeated Champion {self.opponent.name}", "S-Next"), ("\nYou are the new Pokemon \nLeague Champion!", "End")]
            self.next_button.configure(state="normal")
        else:
            self.next_text = [(f"{self.player.name} is out of usable pokemon", "S-Next"), (f"\n{self.player.name} whited out!", "End")]
            self.next_button.configure(state="normal")

    def update_font_size(self, event):
        if event.widget == self.window:
            new_size = min(event.width // 20, event.height // 20)
            new_font = (self.current_font[0], new_size, self.current_font[2])
            self.configure(font=new_font)