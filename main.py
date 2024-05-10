#Main file for Calculator
import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry = ('375x667')
        self.window.title('Calculator')

    def run(self):
        self.window.mainloop()
