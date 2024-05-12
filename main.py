# Main file for Calculator
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class Calculator_UA:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('400x520')
        self.window.title('Calculator UA')
        self.expression = ''
        self.total_expression = ''

        self.calculation_frame = self.create_calculation_frame()
        self.display_label = self.create_display_label()
        self.buttons_frame = self.create_buttons_frame()

        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), '.': (4,3)
        }
        self.operations = {'/': '\u00f7', '*': '\u00d7', '-': '-', '+': '+'}

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_buttons()

    def create_buttons(self):
        self.create_operations_buttons()
        self.create_equal_button()
        self.create_digits_buttons()
        self.create_parentheses_buttons()
        self.create_all_clear_button()
        self.create_clear_button()

    def create_display_label(self):
        label = Label(self.calculation_frame, text=self.expression, anchor=E, fg='black', bg='lightgray', font=('Arial', 24, 'bold'))
        label.pack(expand=True, fill='both')
        return label
    
    def create_calculation_frame(self):
        frame = Frame(self.window, height='200')
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        frame = Frame(self.window, height='320')
        frame.pack(expand=True, fill='both')
        return frame

    def create_digits_buttons(self):
        for digit, grid_value in self.digits.items():
            button = Button(self.buttons_frame, text=str(digit), borderwidth=0, font=('Arial', 24, 'bold'), command=lambda x=digit: self.update_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)

    def create_operations_buttons(self):
        i = 0

        for operator, symbol in self.operations.items():
            button = Button(self.buttons_frame, text=symbol, borderwidth=0, font=('Arial', 24, 'bold'), command=lambda x=symbol: self.append_operator(x))
            button.grid(row=i, column=4, sticky=NSEW)
            i += 1

    def create_equal_button(self):
        button = Button(self.buttons_frame, text='=', borderwidth=0, font=('Arial', 24, 'bold'), command=lambda: self.evaluation())
        button.grid(row=4, column=4, sticky=NSEW)

    def create_parentheses_buttons(self):
        button_1 = Button(self.buttons_frame, text='(', borderwidth=0, font=('Arial', 24, 'bold'), command=lambda: self.update_expression('('))
        button_1.grid(row=0, column=2, sticky=NSEW)
        button_2 = Button(self.buttons_frame, text=')', borderwidth=0, font=('Arial', 24, 'bold'), command=lambda: self.update_expression(')'))
        button_2.grid(row=0, column=3, sticky=NSEW)

    def create_all_clear_button(self):
        button = Button(self.buttons_frame, text='C', borderwidth=0, font=('Arial', 24, 'bold'), command=lambda: self.all_clear())
        button.grid(row=0, column=1, sticky=NSEW)

    def create_clear_button(self):
        button = Button(self.buttons_frame, text='<<', borderwidth=0, font=('Arial', 24, 'bold'), command=lambda: self.clear())
        button.grid(row=4, column=1, sticky=NSEW)
        
    def update_label(self):
        self.display_label.config(text=self.expression)

    def update_expression(self, value):
        self.expression += str(value)
        self.total_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.total_expression += operator
        self.expression = ''
        self.update_label()

    def all_clear(self):
        self.expression = ''
        self.update_label()

    def clear(self):
        self.expression = self.expression[:-1]
        self.update_label()

    def evaluation(self):
        self.expression = str(eval(self.total_expression))
        self.update_label()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator_ua = Calculator_UA()
    calculator_ua.run()
