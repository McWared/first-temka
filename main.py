# Main file for Calculator
import tkinter as tk


class Calculator_UA:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry = '500x800'
        self.window.title('Calculator UA')

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator_ua = Calculator_UA()
    calculator_ua.run()
