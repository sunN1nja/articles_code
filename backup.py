import os
import shutil
import datetime

def create_backup(source_directory, backup_directory):
    # Проверяем, существует ли исходный каталог
    if not os.path.exists(source_directory):
        print(f"Исходный каталог '{source_directory}' не существует.")
        return

    # Создаем каталог резервного копирования с текущей датой и временем
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_path = os.path.join(backup_directory, f"backup_{current_time}")
    os.makedirs(backup_path)

    # Копируем файлы и папки из исходного каталога в каталог резервного копирования
    for item in os.listdir(source_directory):
        source_item = os.path.join(source_directory, item)
        backup_item = os.path.join(backup_path, item)
        
        if os.path.isdir(source_item):
            shutil.copytree(source_item, backup_item)
        else:
            shutil.copy2(source_item, backup_item)
    
    print(f"Резервное копирование завершено. Файлы и папки скопированы в '{backup_path}'")

if __name__ == "__main__":
    # Указываем исходный каталог и каталог для резервного копирования
    source_directory = input("Введите путь к исходному каталогу: ")
    backup_directory = input("Введите путь к каталогу для резервного копирования: ")

    create_backup(source_directory, backup_directory)