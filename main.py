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

        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), '.': (4,3)
        }
        self._create_digits_buttons()

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


    def _create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = Button(self.buttons_frame, text=str(digit))
            button.grid(column=grid_value[1], row=grid_value[0])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator_ua = Calculator_UA()
    calculator_ua.run()
