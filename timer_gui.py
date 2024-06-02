import time
import os
import platform
import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.time_left_var = tk.StringVar()
        self.time_left_var.set("00:00")
        self.create_widgets()
        self.os_type = platform.system()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter time in seconds:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.time_left_label = tk.Label(self.root, textvariable=self.time_left_var, font=("Helvetica", 48))
        self.time_left_label.pack()

    def start_timer(self):
        try:
            total_seconds = int(self.entry.get())
            self.countdown(total_seconds)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number of seconds")

    def countdown(self, seconds):
        if seconds:
            mins, secs = divmod(seconds, 60)
            self.time_left_var.set(f"{mins:02d}:{secs:02d}")
            self.root.after(1000, self.countdown, seconds - 1)
        else:
            self.time_left_var.set("00:00")
            self.play_sound()

    def play_sound(self):
        if self.os_type == "Windows":
            import winsound
            winsound.Beep(1000, 1000)
        elif self.os_type == "Darwin":  # macOS
            os.system('afplay /System/Library/Sounds/Glass.aiff')
        elif self.os_type == "Linux":
            os.system('aplay /usr/share/sounds/alsa/Front_Center.wav')
        else:
            messagebox.showinfo("Time's up!", "Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
