import os
import tkinter as tk
from tkinter import filedialog, Listbox, END, messagebox
import pygame

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")
        self.root.geometry("400x300")

        self.playlist = Listbox(self.root, selectmode=tk.SINGLE, bg="black", fg="white", font=('arial', 15), width=40)
        self.playlist.pack(pady=20)

        self.load_button = tk.Button(self.root, text="Load Folder", command=self.load_folder)
        self.load_button.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        pygame.mixer.init()

    def load_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.playlist.delete(0, END)
            self.music_files = [os.path.join(folder_selected, file) for file in os.listdir(folder_selected) if file.endswith('.mp3')]
            if not self.music_files:
                messagebox.showinfo("No Music Files", "No .mp3 files found in the selected folder.")
                return
            
            for file in self.music_files:
                self.playlist.insert(END, os.path.basename(file))
        else:
            messagebox.showinfo("No Folder Selected", "Please select a folder to load music files from.")

    def play_music(self):
        selected_song_index = self.playlist.curselection()
        if selected_song_index:
            selected_song = self.music_files[selected_song_index[0]]
            try:
                pygame.mixer.music.load(selected_song)
                pygame.mixer.music.play()
            except Exception as e:
                messagebox.showerror("Error", f"Could not play the selected song. Error: {e}")
        else:
            messagebox.showinfo("No Song Selected", "Please select a song to play.")

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()
