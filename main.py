"""Main file for Calculator"""
from tkinter import *

class CalculatorUA:
    """Calculator class that defining all stuff"""

    def __init__(self) -> None:
        """
        Init object
        """
        self.window = Tk()
        self.window.geometry('400x520')
        self.window.title('Calculator UA')
        self.expression = ''
        self.total_expression = ''
        self.is_UNAR_OPERATOR = False
        self.is_OPERATOR = False
        self.is_DOT = False
        # self.is_PARENTHESES = False
        self.is_ERROR = False

        self.calculation_frame = self.create_calculation_frame()
        self.display_label = self.create_display_label()
        self.buttons_frame = self.create_buttons_frame()

        self.digits = {
            '7': (1, 1), '8': (1, 2), '9': (1, 3),
            '4': (2, 1), '5': (2, 2), '6': (2, 3),
            '1': (3, 1), '2': (3, 2), '3': (3, 3),
            '0': (4, 2)
        }
        self.operations = {'/': '\u00f7', '*': '\u00d7', '-': '-', '+': '+'}
        self.unar_operations = {'-': '-', '+': '+'}

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_buttons()

    def create_buttons(self) -> None:
        """
        Creates all buttons
        """
        self.create_operations_buttons()
        self.create_equal_button()
        self.create_dot_button()
        self.create_digits_buttons()
        self.create_parentheses_buttons()
        self.create_all_clear_button()
        self.create_clear_button()

    def create_display_label(self) -> Label:
        """
        Creates display label
        """
        label = Label(self.calculation_frame, text=self.expression, anchor=E, fg='black', bg='lightgray',
                      font=('Arial', 24, 'bold'))
        label.pack(expand=True, fill='both')
        return label

    def create_calculation_frame(self) -> Frame:
        """
        Creates frame for the expression area
        """
        frame = Frame(self.window, height='200')
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self) -> Frame:
        """
        Creates frame for the buttons area
        """
        frame = Frame(self.window, height='320')
        frame.pack(expand=True, fill='both')
        return frame

    def create_digits_buttons(self) -> None:
        """
        Creates buttons for all digits
        """
        for digit, grid_value in self.digits.items():
            button = Button(self.buttons_frame, text=str(digit), borderwidth=0, font=('Arial', 24, 'bold'),
                            command=lambda x=digit: self.update_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)

    def create_operations_buttons(self) -> None:
        """
        Creates buttons for all operators
        """
        i = 0

        for operator, symbol in self.operations.items():
            button = Button(self.buttons_frame, text=symbol, borderwidth=0, font=('Arial', 24, 'bold'),
                            command=lambda x=symbol, y=operator: self.append_operator(x, y))
            button.grid(row=i, column=4, sticky=NSEW)
            i += 1

    def create_equal_button(self) -> None:
        """
        Creates button for equal
        """
        button = Button(self.buttons_frame, text='=', borderwidth=0, font=('Arial', 24, 'bold'),
                        command=lambda: self.evaluation())
        button.grid(row=4, column=4, sticky=NSEW)

    def create_dot_button(self) -> None:
        """
        Creates button for dot
        """
        button = Button(self.buttons_frame, text='.', borderwidth=0, font=('Arial', 24, 'bold'),
                        command=lambda: self.append_dot('.'))
        button.grid(row=4, column=3, sticky=NSEW)

    def create_parentheses_buttons(self) -> None:
        """
        Creates buttons for parentheses
        """
        button_1 = Button(self.buttons_frame, text='(', borderwidth=0, font=('Arial', 24, 'bold'),
                          command=lambda: self.update_expression('('))
        button_1.grid(row=0, column=2, sticky=NSEW)
        button_2 = Button(self.buttons_frame, text=')', borderwidth=0, font=('Arial', 24, 'bold'),
                          command=lambda: self.update_expression(')'))
        button_2.grid(row=0, column=3, sticky=NSEW)

    def create_all_clear_button(self) -> None:
        """
        Creates button for all clear
        """
        button = Button(self.buttons_frame, text='C', borderwidth=0, font=('Arial', 24, 'bold'),
                        command=lambda: self.all_clear())
        button.grid(row=0, column=1, sticky=NSEW)

    def create_clear_button(self) -> None:
        """
        Creates button for clear the last symbol
        """
        button = Button(self.buttons_frame, text='<<', borderwidth=0, font=('Arial', 24, 'bold'),
                        command=lambda: self.clear())
        button.grid(row=4, column=1, sticky=NSEW)

    def update_label(self) -> None:
        """
        Updates the text on the label
        """
        self.display_label.config(text=self.expression)

#TODO: you cannot place a parenth after a dot
#TODO: unar minus
    def update_expression(self, value) -> None:
        """
        Updates the expression, adding new symbols to it
        - args: 
            value: str | int
        """
        if not self.is_ERROR:
            if value == '(':
                self.first_parentheses_check()
            else:
                self.is_OPERATOR = False
                self.expression += str(value)
                self.total_expression += str(value)
                self.update_label()

    def append_operator(self, symbol, operator) -> None:
        """
        Updates the expression, adding new operator symbol to it
        - args: 
            operator: str
        """
        if not self.is_ERROR:
            if not self.is_OPERATOR:
                self.is_OPERATOR = True
                self.is_DOT = False
                self.expression += symbol
                self.total_expression += operator
                self.update_label()

    def append_dot(self, dot) -> None:
        """
        Updates the expression, adding new dot
        """
        if not self.is_ERROR:
            if not self.is_DOT:
                self.is_DOT = True
                self.expression += dot
                self.total_expression += dot
                self.update_label()

    def clear_variables(self) -> None:
        self.expression = ''
        self.total_expression = ''
        self.is_DOT = False
        self.is_OPERATOR = False
        self.is_ERROR = False

    def all_clear(self) -> None:
        """
        Full clears the expression
        """
        self.clear_variables()
        self.update_label()

    def clear(self) -> None:
        """
        Deletes the last symbol in the expression
        """
        if not self.is_ERROR:
            self.expression = self.expression[:-1]
            self.total_expression = self.total_expression[:-1]
            if self.total_expression[-1] == '.':
                self.is_DOT = False
            if self.total_expression[-1] in self.operations:
                self.is_OPERATOR = False
            self.update_label()

    def evaluation(self) -> None:
        """
        Evaluates the expression
        """
        try:
            self.expression = str(round(eval(self.total_expression), 10))
            self.total_expression = self.expression
            self.update_label()
        except BaseException as e:
            self.catch_errors(e)

    def catch_errors(self, e):
        msg_forward = "'(' was never closed"
        msg_backward = "unmatched ')'"
        if msg_forward in str(e):
            self.total_expression += ')'
            self.evaluation()
        elif msg_backward in str(e):
            self.total_expression = '(' + self.total_expression
            self.evaluation()
        else:
            self.expression = 'Error'
            self.is_ERROR = True
            self.update_label()

    def first_parentheses_check(self):
        if self.total_expression[-1] in self.digits or self.total_expression[-1] in self.operations:
            if self.total_expression[-1] in self.digits or self.total_expression[-1] == ')':
                self.total_expression += "*"
            self.is_OPERATOR = False
            self.total_expression += str("(")
            self.expression += str("(")
            self.update_label()

    def run(self) -> None:
        """
        Runs the window
        """
        self.window.mainloop()


if __name__ == "__main__":
    calculator_ua = CalculatorUA()
    calculator_ua.run()
