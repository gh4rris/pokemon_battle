import customtkinter as ctk
import time

class Battle(ctk.CTkLabel):
    def __init__(self, frame, window):
        super().__init__(frame)
        self.frame = frame
        self.window = window
        self.string_var = ctk.StringVar()
        self.current_font = ("Arial", min(self.window.width // 25, self.window.height // 25), "bold")
        self.configure(textvariable=self.string_var, anchor="nw", font=self.current_font)
        self.window.bind("<Configure>", self.update_font_size)
        self.grid(row=0, column=0, sticky="nsew", rowspan=2, padx=10, pady=10)
        self.next_button = ctk.CTkButton(frame, text="Next", command=self.progress_text, anchor="se")
        self.next_button.place(relx=0.6, rely=1, relwidth=0.2, relheight=0.3, anchor="se")

    def oppening_battle(self, trainer, opponent):
        current_text = ""
        new_text = f"Champion {opponent.name} wants to battle!"
        for i in new_text:
            self.string_var.set(current_text + i)
            current_text = self.string_var.get()
            self.frame.update()
            time.sleep(0.03)

    def progress_text(self):
        pass

    def update_font_size(self, event):
        if event.widget == self.window:
            new_size = min(event.width // 25, event.height // 25)
            new_font = (self.current_font[0], new_size, self.current_font[2])
            self.configure(font=new_font)
            # print(f"width: {event.width} height: {event.height}")
            # print(event)