import tkinter as tk
import os
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.playlist = []
        self.current_song = 0

        # Initialize Pygame mixer
        mixer.init()

        # Create GUI elements
        self.song_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.song_listbox.pack(pady=10)

        self.select_button = tk.Button(self.root, text="Select Song", command=self.select_song)
        self.select_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_song)
        self.next_button.pack(pady=5)

        self.previous_button = tk.Button(self.root, text="Previous", command=self.previous_song)
        self.previous_button.pack(pady=5)

    def select_song(self):
        song_path = filedialog.askopenfilename(title="Select Song", filetypes=[("MP3 Files", "*.mp3")])
        if song_path:
            self.playlist.append(song_path)
            self.song_listbox.insert(tk.END, os.path.basename(song_path))

    def play(self):
        if self.playlist:
            song_path = self.playlist[self.current_song]
            mixer.music.load(song_path)
            mixer.music.play()

    def stop(self):
        mixer.music.stop()

    def next_song(self):
        if self.playlist:
            self.current_song = (self.current_song + 1) % len(self.playlist)
            self.play()

    def previous_song(self):
        if self.playlist:
            self.current_song = (self.current_song - 1) % len(self.playlist)
            self.play()

# Create the Tkinter application window
root = tk.Tk()

# Create the music player
player = MusicPlayer(root)

# Run the Tkinter event loop
root.mainloop()
