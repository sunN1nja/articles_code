import os

# Функция для создания новой заметки
def create_note():
    filename = input("Введите название файла (без расширения): ") + ".txt"
    with open(filename, "w") as file:
        content = input("Введите содержимое заметки:\n")
        file.write(content)
    print("Заметка сохранена.")

# Функция для просмотра содержимого заметки
def view_note():
    filename = input("Введите название файла, который хотите прочитать (без расширения): ") + ".txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            print(file.read())
    else:
        print("Файл не найден.")

# Функция для удаления заметки
def delete_note():
    filename = input("Введите название файла, который хотите удалить (без расширения): ") + ".txt"
    if os.path.exists(filename):
        os.remove(filename)
        print("Заметка удалена.")
    else:
        print("Файл не найден.")

# Главное меню приложения
def main_menu():
    while True:
        print("\nБлокнот")
        print("1. Создать заметку")
        print("2. Просмотреть заметку")
        print("3. Удалить заметку")
        print("4. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            create_note()
        elif choice == "2":
            view_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main_menu()