# Main file for Calculator
import tkinter as tk


class Calculator_UA:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('400x520')
        self.window.title('Calculator UA')

    def _create_calculation_frame(self):
        pass

    def _create_buttons_frame(self):
        pass

    def _create_buttons(self):
        pass

    def run(self):
        self._create_calculation_frame()
        self._create_buttons_frame()
        self.window.mainloop()


if __name__ == "__main__":
    calculator_ua = Calculator_UA()
    calculator_ua.run()
