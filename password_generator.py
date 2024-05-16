import random
import string

def generate_password(length=12):
    # Символы, которые можно использовать в пароле
    chars = string.ascii_letters + string.digits + string.punctuation
    # Генерация случайного пароля
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Пример использования функции
if __name__ == "__main__":
    length = int(input("Введите длину пароля: "))
    print(f"Сгенерированный пароль: {generate_password(length)}")