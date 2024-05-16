import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound


def play_sound():
    for _ in range(3):  # Проиграть звук 3 раза
        winsound.Beep(2500, 1000)  # Частота 2500 Гц, длительность 1000 мс

def countdown(t, label):
    while t > -1:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        time.sleep(1)
        t -= 1
    play_sound()

def start_pomodoro(work_time, short_break, long_break, cycles, label):
    completed_cycles = 0
    while True:
        label.config(text="Работаем!")
        countdown(work_time * 60, label)
        completed_cycles += 1

        if completed_cycles % cycles == 0:
            label.config(text="Время длинного перерыва!")
            countdown(long_break * 60, label)
        else:
            label.config(text="Время короткого перерыва!")
            countdown(short_break * 60, label)

def start_thread(work_time, short_break, long_break, cycles, label):
    threading.Thread(target=start_pomodoro, args=(work_time, short_break, long_break, cycles, label)).start()

def main():
    root = tk.Tk()
    root.title("Таймер Pomodoro")

    label = tk.Label(root, text="Нажмите 'Старт'", font=("Arial", 48))
    label.pack()

    start_button = tk.Button(root, text="Старт", command=lambda: start_thread(25, 5, 15, 4, label), font=("Arial", 24))
    start_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()