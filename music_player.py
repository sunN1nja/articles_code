import os
import tkinter as tk
from tkinter import filedialog, Listbox, END, messagebox
from pydub import AudioSegment
from pydub.playback import play
import threading

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")
        self.root.geometry("400x500")

        self.current_song_index = None
        self.music_files = []
        self.currently_playing_thread = None
        self.stop_event = threading.Event()

        self.playlist = Listbox(self.root, selectmode=tk.SINGLE, bg="black", fg="white", font=('arial', 12), width=60)
        self.playlist.pack(pady=20)

        self.load_file_button = tk.Button(self.root, text="Load File", command=self.load_file)
        self.load_file_button.pack(pady=5)

        self.load_folder_button = tk.Button(self.root, text="Load Folder", command=self.load_folder)
        self.load_folder_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_song)
        self.next_button.pack(pady=5)

        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_song)
        self.prev_button.pack(pady=5)

    def load_file(self):
        file_selected = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_selected:
            self.playlist.insert(END, os.path.basename(file_selected))
            self.music_files.append(file_selected)

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
            self.current_song_index = selected_song_index[0]
            selected_song = self.music_files[self.current_song_index]
            try:
                if self.currently_playing_thread and self.currently_playing_thread.is_alive():
                    self.stop_music()
                self.stop_event.clear()
                audio = AudioSegment.from_mp3(selected_song)
                self.currently_playing_thread = threading.Thread(target=self.play_audio, args=(audio,))
                self.currently_playing_thread.start()
            except Exception as e:
                messagebox.showerror("Error", f"Could not play the selected song. Error: {e}")
        else:
            messagebox.showinfo("No Song Selected", "Please select a song to play.")

    def play_audio(self, audio):
        play(audio)
        if not self.stop_event.is_set():
            self.root.after(100, self.next_song)

    def stop_music(self):
        if self.currently_playing_thread and self.currently_playing_thread.is_alive():
            self.stop_event.set()
            self.currently_playing_thread.join()

    def next_song(self):
        if self.current_song_index is not None:
            self.current_song_index += 1
            if self.current_song_index >= len(self.music_files):
                self.current_song_index = 0
            self.playlist.selection_clear(0, END)
            self.playlist.selection_set(self.current_song_index)
            self.playlist.activate(self.current_song_index)
            self.play_music()

    def prev_song(self):
        if self.current_song_index is not None:
            self.current_song_index -= 1
            if self.current_song_index < 0:
                self.current_song_index = len(self.music_files) - 1
            self.playlist.selection_clear(0, END)
            self.playlist.selection_set(self.current_song_index)
            self.playlist.activate(self.current_song_index)
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()