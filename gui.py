import customtkinter as ctk
from main import run_all
import threading

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI Code Agent")
        self.geometry("900x600")

        self.input = ctk.CTkTextbox(self)
        self.input.pack(fill="both", expand=True, padx=10, pady=10)

        self.btn = ctk.CTkButton(self, text="运行", command=self.start)
        self.btn.pack(pady=5)

        self.output = ctk.CTkTextbox(self)
        self.output.pack(fill="both", expand=True, padx=10, pady=10)

    def start(self):
        threading.Thread(target=self.run).start()

    def run(self):
        res = run_all(self.input.get("1.0","end"))
        self.output.delete("1.0","end")
        self.output.insert("end", str(res))

App().mainloop()
