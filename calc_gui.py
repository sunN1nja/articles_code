import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)

        self.expression = ""
        self.text_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Создание текстового поля для ввода выражений
        entry = tk.Entry(self.root, font=('arial', 24, 'bold'), textvariable=self.text_input, bd=30, insertwidth=4,
                         bg="white", fg="black", justify='right')
        entry.grid(columnspan=4)

        # Создание кнопок
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            self.create_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Кнопка для очистки
        clear_button = tk.Button(self.root, text='C', padx=20, pady=20, bd=8, fg="white", bg="red",
                                 font=('arial', 20, 'bold'), command=self.clear)
        clear_button.grid(row=row, column=col, columnspan=4, sticky="nsew")

    def create_button(self, value, row, col):
        button = tk.Button(self.root, text=value, padx=20, pady=20, bd=8, fg="black", bg="light gray",
                           font=('arial', 20, 'bold'), command=lambda: self.on_button_click(value))
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, value):
        if value == "=":
            try:
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except:
                self.text_input.set("Ошибка")
                self.expression = ""
        else:
            self.expression += value
            self.text_input.set(self.expression)

    def clear(self):
        self.expression = ""
        self.text_input.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()