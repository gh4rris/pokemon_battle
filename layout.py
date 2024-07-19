import customtkinter as ctk
from battle import Battle
import time

class Window(ctk.CTk):
    def __init__(self, name, size, player, opponent):
        super().__init__()
        self.title(name)
        self.width = size[0]
        self.height = size[1]
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(self.width, self.height)
        self.text_action_frame = TextActionFrame(self)
        self.start_button = ctk.CTkButton(self, text="Start", corner_radius=100, font=("Arial", 30, "bold"), command=lambda: self.start_game(player, opponent))
        self.start_button.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.player_bar = PlayerHealthBar(self, player)
        self.opponent_bar = OpponentHealthBar(self, opponent)
        self.mainloop()

    def start_game(self, player, opponent):
        self.start_button.place_forget()
        battle = Battle(self.text_action_frame, self, player, opponent).oppening_battle(player, opponent)


class TextActionFrame(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.place(relx=0, rely=0.65, relwidth=1, relheight=0.35)
        self.grid_columnconfigure(0, weight=3, uniform="a")
        self.grid_columnconfigure((1, 2), weight=1, uniform="a")
        self.grid_rowconfigure((0, 1), weight=1, uniform="a")


class PlayerHealthBar(ctk.CTkFrame):
    def __init__(self, window, player):
        super().__init__(window)
        self.grid_rowconfigure((0, 1, 2), weight=1, uniform="a")
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.player = player
        self.name_label_var = ctk.StringVar()
        self.health_bar_var = ctk.DoubleVar()
        self.health_label_var = ctk.StringVar()
        self.name_label = ctk.CTkLabel(self, textvariable=self.name_label_var, font=("Arial", min(window.width // 25, window.height // 25), "bold"))
        self.health_bar = ctk.CTkProgressBar(self, height=20, variable=self.health_bar_var)
        self.health_label = ctk.CTkLabel(self, textvariable=self.health_label_var, font=("Arial", min(window.width // 25, window.height // 25), "bold"))
        self.lvl_label = ctk.CTkLabel(self, font=("Arial", min(window.width // 35, window.height // 35), "bold"))
        player.health_bar = self
        

    def place_widgets(self):
        self.name_label_var.set(self.player.out.name)
        self.health_bar_var.set(round(self.player.out.hp / self.player.out.max_hp, 2))
        self.health_label_var.set(f"{self.player.out.hp} / {self.player.out.max_hp}")
        self.lvl_label.configure(text=f"Lvl {self.player.out.lvl}")
        self.name_label.grid(row=0, column=0, columnspan=3, sticky="s")
        self.health_bar.grid(row=1, column=0, columnspan=3, sticky="we", padx=20)
        self.health_label.grid(row=2, column=0, columnspan=3, sticky="n")
        self.lvl_label.grid(row=0, column=2, sticky="s")
        self.place(relx=0.6, rely=0.325, relwidth=0.4, relheight=0.325)

    def change_hp(self):
        if self.player.out.hp > 0:
            new_hp = round(self.player.out.hp / self.player.out.max_hp, 2)
        else:
            new_hp = 0
        self.animate_hp_bar(new_hp)
        self.animate_hp_text(self.player.out.hp)

    def animate_hp_bar(self, new_hp):
        current_hp = self.health_bar_var.get()
        if current_hp < new_hp:
            new_value = min(current_hp + 0.01, new_hp)
            self.health_bar_var.set(new_value)
            self.after(30, self.animate_hp_bar, new_hp)
        elif current_hp > new_hp:
            new_value = max(current_hp - 0.01, new_hp)
            self.health_bar_var.set(new_value)
            self.after(30, self.animate_hp_bar, new_hp)
    
    def animate_hp_text(self, new_hp):
        current_hp = int(self.health_label_var.get().split("/")[0])
        if current_hp < new_hp:
            new_value = min(current_hp + 1, new_hp)
            self.health_label_var.set(f"{new_value} / {self.player.out.max_hp}")
            self.after(20, self.animate_hp_text, new_hp)
        elif current_hp > new_hp:
            new_value = max(current_hp - 1, new_hp)
            self.health_label_var.set(f"{new_value} / {self.player.out.max_hp}")
            self.after(20, self.animate_hp_text, new_hp)


class OpponentHealthBar(ctk.CTkFrame):
    def __init__(self, window, opponent):
        super().__init__(window)
        self.grid_rowconfigure((0, 1, 2), weight=1, uniform="a")
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.opponent = opponent
        self.name_label_var = ctk.StringVar()
        self.health_bar_var = ctk.DoubleVar()
        self.health_label_var = ctk.StringVar()
        self.name_label = ctk.CTkLabel(self, textvariable=self.name_label_var, font=("Arial", min(window.width // 25, window.height // 25), "bold"))
        self.health_bar = ctk.CTkProgressBar(self, height=20, variable=self.health_bar_var)
        self.health_label = ctk.CTkLabel(self, textvariable=self.health_label_var, font=("Arial", min(window.width // 25, window.height // 25), "bold"))
        self.lvl_label = ctk.CTkLabel(self, font=("Arial", min(window.width // 35, window.height // 35), "bold"))
        opponent.health_bar = self
        

    def place_widgets(self):
        self.name_label_var.set(self.opponent.out.name)
        self.health_bar_var.set(self.opponent.out.hp / self.opponent.out.max_hp)
        self.health_label_var.set(f"{self.opponent.out.hp} / {self.opponent.out.max_hp}")
        self.lvl_label.configure(text=f"Lvl {self.opponent.out.lvl}")
        self.name_label.grid(row=0, column=0, columnspan=3, sticky="s")
        self.health_bar.grid(row=1, column=0, columnspan=3, sticky="we", padx=20)
        self.health_label.grid(row=2, column=0, columnspan=3, sticky="n")
        self.lvl_label.grid(row=0, column=2, sticky="s")
        self.place(relx=0, rely=0, relwidth=0.4, relheight=0.325)

    def change_hp(self):
        if self.opponent.out.hp > 0:
            new_hp = round(self.opponent.out.hp / self.opponent.out.max_hp, 2)
        else:
            new_hp = 0
        self.animate_hp(new_hp)
        self.animate_hp_text(self.opponent.out.hp)

    def animate_hp(self, new_hp):
        current_hp = self.health_bar_var.get()
        if current_hp < new_hp:
            new_value = min(current_hp + 0.01, new_hp)
            self.health_bar_var.set(new_value)
            self.after(30, self.animate_hp, new_hp)
        elif current_hp > new_hp:
            new_value = max(current_hp - 0.01, new_hp)
            self.health_bar_var.set(new_value)
            self.after(30, self.animate_hp, new_hp)

    def animate_hp_text(self, new_hp):
        current_hp = int(self.health_label_var.get().split("/")[0])
        if current_hp < new_hp:
            new_value = min(current_hp + 1, new_hp)
            self.health_label_var.set(f"{new_value} / {self.opponent.out.max_hp}")
            self.after(20, self.animate_hp_text, new_hp)
        elif current_hp > new_hp:
            new_value = max(current_hp - 1, new_hp)
            self.health_label_var.set(f"{new_value} / {self.opponent.out.max_hp}")
            self.after(20, self.animate_hp_text, new_hp)