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
    if not amount.isdigit():
        messagebox.showerror("Ошибка", "Сумма должна быть числом.")
        return

    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transactions (type, amount, description, date) VALUES (?, ?, ?, ?)',
                   (type, float(amount), description, date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Запись успешно добавлена.")

def update_transaction(id, type, amount, description, date):
    if not amount.isdigit():
        messagebox.showerror("Ошибка", "Сумма должна быть числом.")
        return

    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE transactions
                      SET type = ?, amount = ?, description = ?, date = ?
                      WHERE id = ?''', (type, float(amount), description, date, id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Запись успешно обновлена.")

def delete_transaction(id):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM transactions WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Запись успешно удалена.")

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

def edit_transaction_window(transaction):
    def submit():
        type = type_entry.get()
        amount = amount_entry.get()
        description = description_entry.get()
        date = date_entry.get()
        update_transaction(transaction[0], type, amount, description, date)
        edit_window.destroy()
        view_transactions_window()

    edit_window = tk.Toplevel(root)
    edit_window.title("Редактировать транзакцию")

    tk.Label(edit_window, text="Тип (доход/расход):").grid(row=0, column=0)
    type_entry = tk.Entry(edit_window)
    type_entry.insert(0, transaction[1])
    type_entry.grid(row=0, column=1)

    tk.Label(edit_window, text="Сумма:").grid(row=1, column=0)
    amount_entry = tk.Entry(edit_window)
    amount_entry.insert(0, transaction[2])
    amount_entry.grid(row=1, column=1)

    tk.Label(edit_window, text="Описание:").grid(row=2, column=0)
    description_entry = tk.Entry(edit_window)
    description_entry.insert(0, transaction[3])
    description_entry.grid(row=2, column=1)

    tk.Label(edit_window, text="Дата (YYYY-MM-DD):").grid(row=3, column=0)
    date_entry = tk.Entry(edit_window)
    date_entry.insert(0, transaction[4])
    date_entry.grid(row=3, column=1)

    submit_btn = tk.Button(edit_window, text="Сохранить", command=submit)
    submit_btn.grid(row=4, column=0, columnspan=2)

def view_transactions_window():
    def edit_transaction():
        selected_item = tree.selection()[0]
        transaction = tree.item(selected_item, 'values')
        edit_transaction_window(transaction)

    def delete_transaction():
        selected_item = tree.selection()[0]
        transaction = tree.item(selected_item, 'values')
        delete_transaction(transaction[0])
        view_window.destroy()
        view_transactions_window()

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

    edit_btn = tk.Button(view_window, text="Редактировать", command=edit_transaction)
    edit_btn.pack(side=tk.LEFT, fill='x', expand=True)

    delete_btn = tk.Button(view_window, text="Удалить", command=delete_transaction)
    delete_btn.pack(side=tk.LEFT, fill='x', expand=True)

def search_transactions_window():
    def search():
        type = type_entry.get()
        date = date_entry.get()
        description = description_entry.get()

        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        query = 'SELECT * FROM transactions WHERE 1=1'
        params = []
        
        if type:
            query += ' AND type = ?'
            params.append(type)
        if date:
            query += ' AND date = ?'
            params.append(date)
        if description:
            query += ' AND description LIKE ?'
            params.append(f'%{description}%')

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()

        for item in tree.get_children():
            tree.delete(item)
        for row in rows:
            tree.insert('', tk.END, values=row)

    search_window = tk.Toplevel(root)
    search_window.title("Поиск транзакций")

    tk.Label(search_window, text="Тип (доход/расход):").grid(row=0, column=0)
    type_entry = tk.Entry(search_window)
    type_entry.grid(row=0, column=1)

    tk.Label(search_window, text="Дата (YYYY-MM-DD):").grid(row=1, column=0)
    date_entry = tk.Entry(search_window)
    date_entry.grid(row=1, column=1)

    tk.Label(search_window, text="Описание:").grid(row=2, column=0)
    description_entry = tk.Entry(search_window)
    description_entry.grid(row=2, column=1)

    search_btn = tk.Button(search_window, text="Поиск", command=search)
    search_btn.grid(row=3, column=0, columnspan=2)

    columns = ('id', 'type', 'amount', 'description', 'date')
    tree = ttk.Treeview(search_window, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
    tree.grid(row=4, column=0, columnspan=2, sticky='nsew')

if __name__ == '__main__':
    init_db()

    root = tk.Tk()
    root.title("Управление финансами")

    add_btn = tk.Button(root, text="Добавить запись", command=add_transaction_window)
    add_btn.pack(fill='x', expand=True)

    view_btn = tk.Button(root, text="Показать все записи", command=view_transactions_window)
    view_btn.pack(fill='x', expand=True)

    search_btn = tk.Button(root, text="Поиск записей", command=search_transactions_window)
    search_btn.pack(fill='x', expand=True)

    root.mainloop()
