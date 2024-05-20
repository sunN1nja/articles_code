import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')  # Вывод времени обратного отсчета в одной строке
        time.sleep(1)
        seconds -= 1
    
    print("Время вышло!")

# Запросите у пользователя время для таймера
total_time = input("Введите время для обратного отсчета в секундах: ")
try:
    total_time = int(total_time)
    countdown_timer(total_time)
except ValueError:
    print("Пожалуйста, введите корректное число секунд.")
