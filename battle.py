import customtkinter as ctk
import time
from action import Fight

class Battle(ctk.CTkLabel):
    def __init__(self, frame, window, trainer, opponent):
        super().__init__(frame)
        self.frame = frame
        self.window = window
        self.string_var = ctk.StringVar()
        self.current_font = ("Arial", min(self.window.width // 20, self.window.height // 20), "bold")
        self.configure(textvariable=self.string_var, anchor="nw", font=self.current_font, justify="left")
        self.window.bind("<Configure>", self.update_font_size)
        self.grid(row=0, column=0, sticky="nsew", rowspan=2, padx=25, pady=25)
        trainer.battle = self
        opponent.battle = self

        # Widgets
        self.fight_button = ctk.CTkButton(self.frame, text="Fight", state="disabled", command=lambda: Fight(self.frame, self, trainer.out, opponent.out))
        self.change_pokemon_button = ctk.CTkButton(self.frame, text="Change Pokemon", state="disabled")
        self.item_button = ctk.CTkButton(self.frame, text="Item", state="disabled")
        self.run_button = ctk.CTkButton(self.frame, text="Run", state="disabled")
        self.next_text = None
        self.next_button = ctk.CTkButton(frame, text="Next", command=lambda: self.progress_text(self.next_text), anchor="se", state="disabled")
        
        self.fight_button.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        self.change_pokemon_button.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
        self.item_button.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        self.run_button.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
        self.next_button.place(relx=0.6, rely=1, relwidth=0.2, relheight=0.3, anchor="se")

    def oppening_battle(self, trainer, opponent):
        trainer.out = trainer.party[0]
        opponent.out = opponent.party[0]
        current_text = ""
        new_text = f"Champion {opponent.name} wants to battle!\n{opponent.name} sent out {opponent.out.name}.\nGo {trainer.out.name}!"
        for i in new_text:
            self.string_var.set(current_text + i)
            current_text = self.string_var.get()
            self.frame.update()
            time.sleep(0.02)
        self.window.trainer_bar.place_widgets()
        self.window.opponent_bar.place_widgets()
        self.next_text = f"What will {trainer.name} do?"
        self.next_button.configure(state="normal")

    def progress_text(self, text):
        self.next_button.configure(state="disabled")
        self.grid_forget()
        self.string_var.set("")
        self.grid(row=0, column=0, sticky="nsew", rowspan=2, padx=25, pady=25)
        current_text = ""
        for i in text:
            self.string_var.set(current_text + i)
            current_text = self.string_var.get()
            self.frame.update()
            time.sleep(0.02)
        self.switch_button_state()

    def switch_button_state(self):
        if self.fight_button._state == "disabled":
            self.fight_button.configure(state="normal")
            self.change_pokemon_button.configure(state="normal")
            self.item_button.configure(state="normal")
            self.run_button.configure(state="normal")
        else:
            self.fight_button.configure(state="disabled")
            self.change_pokemon_button.configure(state="disabled")
            self.item_button.configure(state="disabled")
            self.run_button.configure(state="disabled")

    def update_font_size(self, event):
        if event.widget == self.window:
            new_size = min(event.width // 20, event.height // 20)
            new_font = (self.current_font[0], new_size, self.current_font[2])
            self.configure(font=new_font)