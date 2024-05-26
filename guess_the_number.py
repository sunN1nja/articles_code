import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуйте угадать его!")

    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1

            if guess < number_to_guess:
                print("Мое число больше.")
            elif guess > number_to_guess:
                print("Мое число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    guess_the_number()