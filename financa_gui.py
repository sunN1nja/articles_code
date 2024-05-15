import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def init_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                      (id INTEGER PRIMARY KEY, type TEXT, amount REAL, description TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def add_transaction(type, amount, description, date):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transactions (type, amount, description, date) VALUES (?, ?, ?, ?)',
                   (type, amount, description, date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Запись успешно добавлена.")

def show_transactions():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_transaction_window():
    def submit():
        type = type_entry.get()
        amount = amount_entry.get()
        description = description_entry.get()
        date = date_entry.get()
        add_transaction(type, amount, description, date)
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Добавить транзакцию")

    tk.Label(add_window, text="Тип (доход/расход):").grid(row=0, column=0)
    type_entry = tk.Entry(add_window)
    type_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Сумма:").grid(row=1, column=0)
    amount_entry = tk.Entry(add_window)
    amount_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Описание:").grid(row=2, column=0)
    description_entry = tk.Entry(add_window)
    description_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Дата (YYYY-MM-DD):").grid(row=3, column=0)
    date_entry = tk.Entry(add_window)
    date_entry.grid(row=3, column=1)

    submit_btn = tk.Button(add_window, text="Добавить", command=submit)
    submit_btn.grid(row=4, column=0, columnspan=2)

def view_transactions_window():
    view_window = tk.Toplevel(root)
    view_window.title("Просмотр транзакций")

    transactions = show_transactions()
    columns = ('id', 'type', 'amount', 'description', 'date')
    tree = ttk.Treeview(view_window, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
    for transaction in transactions:
        tree.insert('', tk.END, values=transaction)
    tree.pack(expand=True, fill='both')

if __name__ == '__main__':
    init_db()

    root = tk.Tk()
    root.title("Управление финансами")

    add_btn = tk.Button(root, text="Добавить запись", command=add_transaction_window)
    add_btn.pack(fill='x', expand=True)

    view_btn = tk.Button(root, text="Показать все записи", command=view_transactions_window)
    view_btn.pack(fill='x', expand=True)

    root.mainloop()