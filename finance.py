import sqlite3

def init_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                      (id INTEGER PRIMARY KEY, type TEXT, amount REAL, description TEXT, date TEXT)''')
    conn.commit()
    conn.close()

init_db()

def add_transaction(type, amount, description, date):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transactions (type, amount, description, date) VALUES (?, ?, ?, ?)',
                   (type, amount, description, date))
    conn.commit()
    conn.close()
    print("Запись успешно добавлена.")

def show_transactions():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            type = input("Тип (доход/расход): ")
            amount = float(input("Сумма: "))
            description = input("Описание: ")
            date = input("Дата (YYYY-MM-DD): ")
            add_transaction(type, amount, description, date)
        elif choice == '2':
            show_transactions()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == '__main__':
    main_menu()