import sqlite3
import os



def create_db():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, lastname TEXT, position TEXT)''')
    conn.commit()
    conn.close()


def add_user(fistname, lastname, position):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, lastname, position) VALUES (?, ?, ?)', (f'{fistname}', f'{lastname}', f'{position}'))
    conn.commit()
    conn.close()



def get_position(position):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    rows = cursor.execute(f'SELECT * FROM users WHERE position = "{position}"').fetchall()
    if rows:
        print(f'Найденны записи с должностью {position}:')
        for row in rows:
            print(row)
    else:
        print(f'Записей с позицией {position} не найдено!')
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f'Пользователь с id {user_id} был успешно удален.')
    else:
        print(f'Пользователь с id {user_id} не найден.')
    conn.close()


if __name__ == '__main__':
    print('Это пример приложения, для работы с БД SQLite')
    print()
    print('Для начала проверим, есть ли бд')
    if os.path.exists('db.sqlite') == True:
        print('Бд существует!')
    else:
        print('Бд нету, сейчас её создам!')
        create_db()
    print()
    print('1 - Добавить рабочего')
    print('2 - Вывести рабочих по должности')
    print('2 - Удалить пользователя по id')
    answer = input('Что будем делать?:')
    if answer == '1':
        fistname = input('Введи имя рабочего: ')
        lastname = input('Введи фамилию рабочего: ')
        position = input('Введи должность рабочего: ')
        add_user(fistname, lastname, position)
        print(f'В бд добавлена запись: {fistname}, {lastname}, {position}')
    elif answer == '2':
        position = input('Введите должность, данные которой вывести на экран: ')
        get_position(position)
    elif answer == '3':
        user_id = input('Введите user_id пользователя, которого нужно удалить из базы данных: ')
        delete_user(user_id)
        print(f'Пользователь с user_id: {user_id} удалён')
    else:
        print('Ты не справился даже с вводом цифры с клавиатуры!')