import customtkinter as ctk

class Window(ctk.CTk):
    def __init__(self, name, size):
        super().__init__()
        self.title(name)
        self.geometry(f"{size[0]}x{size[1]}")
        TextActionFrame(self)
        self.mainloop()


class TextActionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0, rely=0.65, relwidth=1, relheight=0.35)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure((1, 2), weight=1, uniform="a")
        self.grid_rowconfigure((0, 1), weight=1, uniform="a")
        ctk.CTkLabel(self, text="Fight", fg_color="red").grid(row=0, column=1, sticky="nsew")