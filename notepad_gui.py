import os
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Функция для создания новой заметки
def create_note():
    filename = simpledialog.askstring("Создать заметку", "Введите название файла (без расширения):")
    if filename:
        filename += ".txt"
        content = simpledialog.askstring("Создать заметку", "Введите содержимое заметки:")
        if content:
            with open(filename, "w") as file:
                file.write(content)
            messagebox.showinfo("Успех", "Заметка сохранена.")
        else:
            messagebox.showwarning("Ошибка", "Содержимое заметки не может быть пустым.")
    else:
        messagebox.showwarning("Ошибка", "Название файла не может быть пустым.")

# Функция для просмотра содержимого заметки
def view_note():
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "r") as file:
            content = file.read()
            messagebox.showinfo("Содержимое заметки", content)
    else:
        messagebox.showwarning("Ошибка", "Файл не найден.")

# Функция для удаления заметки
def delete_note():
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        os.remove(filename)
        messagebox.showinfo("Успех", "Заметка удалена.")
    else:
        messagebox.showwarning("Ошибка", "Файл не найден.")

# Функция для поиска заметок по имени
def search_note():
    keyword = simpledialog.askstring("Поиск заметки", "Введите ключевое слово для поиска:")
    if keyword:
        notes = [f for f in os.listdir() if f.endswith(".txt") and keyword in f]
        if notes:
            messagebox.showinfo("Результаты поиска", "\n".join(notes))
        else:
            messagebox.showinfo("Результаты поиска", "Заметки не найдены.")
    else:
        messagebox.showwarning("Ошибка", "Ключевое слово не может быть пустым.")

# Функция для поиска по содержимому заметок
def search_note_content():
    keyword = simpledialog.askstring("Поиск по содержимому", "Введите ключевое слово для поиска по содержимому:")
    if keyword:
        notes = [f for f in os.listdir() if f.endswith(".txt")]
        found_notes = []
        for note in notes:
            with open(note, "r") as file:
                content = file.read()
                if keyword in content:
                    found_notes.append(note)
        if found_notes:
            messagebox.showinfo("Результаты поиска", "\n".join(found_notes))
        else:
            messagebox.showinfo("Результаты поиска", "Заметки не найдены.")
    else:
        messagebox.showwarning("Ошибка", "Ключевое слово не может быть пустым.")

# Главное меню приложения
def main_menu():
    root = tk.Tk()
    root.title("Блокнот")

    tk.Button(root, text="Создать заметку", command=create_note).pack(pady=10)
    tk.Button(root, text="Просмотреть заметку", command=view_note).pack(pady=10)
    tk.Button(root, text="Удалить заметку", command=delete_note).pack(pady=10)
    tk.Button(root, text="Поиск заметок по имени", command=search_note).pack(pady=10)
    tk.Button(root, text="Поиск по содержимому заметок", command=search_note_content).pack(pady=10)
    tk.Button(root, text="Выйти", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
