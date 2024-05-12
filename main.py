# Main file for Calculator
from tkinter import *
from tkinter import ttk

class Calculator_UA:
    def __init__(self):
        self.window = Tk()
        self.window.configure(background='white')
        self.window.geometry('400x520')
        self.window.title('Calculator UA')

        self.expression = '0'
        self.calculation_frame = self._create_calculation_frame()

        self.display_label = self._create_display_label()
        self.buttons_frame = self._create_buttons_frame()

    def _create_display_label(self):
        label = Label(self.calculation_frame, text=self.expression, anchor=E, fg='black', bg='lightgray', font='Arial')
        label.pack(expand=True, fill='both')
        return label

    def _create_calculation_frame(self):
        frame = Frame(self.window, height='200')
        frame.pack(expand=True, fill='both')
        return frame

    def _create_buttons_frame(self):
        frame = Frame(self.window, height='320')
        frame.pack(expand=True, fill='both')
        return frame


    def _create_buttons(self):
        pass

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator_ua = Calculator_UA()
    calculator_ua.run()
