import time
import sys

def start_pomodoro(work_time=25, short_break=5, long_break=15, cycles=4):
    """
    Запускает таймер Pomodoro с заданными параметрами.

    :param work_time: Длительность работы в минутах.
    :param short_break: Длительность короткого перерыва в минутах.
    :param long_break: Длительность длинного перерыва в минутах.
    :param cycles: Количество циклов до длинного перерыва.
    """
    completed_cycles = 0

    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

    try:
        while True:
            print("Работаем!")
            countdown(work_time * 60)
            completed_cycles += 1

            if completed_cycles % cycles == 0:
                print("Время длинного перерыва!")
                countdown(long_break * 60)
            else:
                print("Время короткого перерыва!")
                countdown(short_break * 60)

    except KeyboardInterrupt:
        print("Pomodoro остановлен. Хорошего дня!")
        sys.exit()

if __name__ == "__main__":
    start_pomodoro()
