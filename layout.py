import customtkinter as ctk
from battle import Battle

class Window(ctk.CTk):
    def __init__(self, name, size, trainer, opponent):
        super().__init__()
        self.title(name)
        self.width = size[0]
        self.height = size[1]
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(self.width, self.height)
        self.text_action_frame = TextActionFrame(self)
        self.start_button = ctk.CTkButton(self, text="Start", corner_radius=100, font=("Helvetica", 30, "bold"), command=lambda: self.start_game(trainer, opponent))
        self.start_button.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.trainer_bar = TrainerHealthBar(self, trainer)
        self.opponent_bar = OpponentHealthBar(self, opponent)
        self.mainloop()

    def start_game(self, trainer, opponent):
        self.start_button.place_forget()
        battle = Battle(self.text_action_frame, self, trainer, opponent).oppening_battle(trainer, opponent)


class TextActionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0, rely=0.65, relwidth=1, relheight=0.35)
        self.grid_columnconfigure(0, weight=3, uniform="a")
        self.grid_columnconfigure((1, 2), weight=1, uniform="a")
        self.grid_rowconfigure((0, 1), weight=1, uniform="a")


class TrainerHealthBar(ctk.CTkFrame):
    def __init__(self, parent, trainer):
        super().__init__(parent)
        self.grid_rowconfigure((0, 1, 2), weight=1, uniform="a")
        self.grid_columnconfigure(0, weight=1, uniform="a")
        self.trainer = trainer
        self.health_bar = ctk.CTkProgressBar(self, height=20)
        
        

    def place_widgets(self):
        name_label = ctk.CTkLabel(self, text=self.trainer.out.name)
        health_label = ctk.CTkLabel(self, text=f"{self.trainer.out.hp} / {self.trainer.out.max_hp}")
        name_label.grid(row=0)
        self.health_bar.set(self.trainer.out.hp)
        self.health_bar.grid(row=1, sticky="we", padx=20)
        health_label.grid(row=2)
        self.place(relx=0.6, rely=0.325, relwidth=0.4, relheight=0.325)

    def change_hp(self):
        self.health_bar.set(self.trainer.out.hp)


class OpponentHealthBar(ctk.CTkFrame):
    def __init__(self, parent, opponent):
        super().__init__(parent)
        self.grid_rowconfigure((0, 1, 2), weight=1, uniform="a")
        self.grid_columnconfigure(0, weight=1, uniform="a")
        self.opponent = opponent
        self.health_bar = ctk.CTkProgressBar(self, height=20)
        

    def place_widgets(self):
        name_label = ctk.CTkLabel(self, text=self.opponent.out.name)
        health_label = ctk.CTkLabel(self, text=f"{self.opponent.out.hp} / {self.opponent.out.max_hp}")
        name_label.grid(row=0)
        self.health_bar.set(self.opponent.out.hp / self.opponent.out.max_hp)
        self.health_bar.grid(row=1, sticky="we", padx=20)
        health_label.grid(row=2)
        self.place(relx=0, rely=0, relwidth=0.4, relheight=0.325)

    def change_hp(self):
        self.health_bar.set(self.opponent.out.hp / self.opponent.out.max_hp)