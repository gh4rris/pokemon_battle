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
        self.mainloop()

    def start_game(self, trainer, opponent):
        self.start_button.place_forget()
        Battle(self.text_action_frame, self).oppening_battle(trainer, opponent)


class TextActionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0, rely=0.65, relwidth=1, relheight=0.35)
        self.grid_columnconfigure(0, weight=3, uniform="a")
        self.grid_columnconfigure((1, 2), weight=1, uniform="a")
        self.grid_rowconfigure((0, 1), weight=1, uniform="a")