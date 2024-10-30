import tkinter as tk
from .navigation import Navigation
from .track_hang import TrackHangPage
from .previous_hangs import PreviousHangsPage

class HangboardApp(Navigation):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Hangboard Timer and Tracker")
        
        # Home screen setup
        self.add_frame(HomePage, "Home")
        self.add_frame(TrackHangPage, "TrackHang")
        self.add_frame(PreviousHangsPage, "PreviousHangs")
        
    def show_home(self):
        self.show_frame("Home")

class HomePage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        tk.Label(self, text="Welcome to Hangboard Tracker", font=("Arial", 16)).pack(pady=10)
        
        track_button = tk.Button(self, text="Track Hang", command=lambda: controller.show_frame("TrackHang"))
        track_button.pack(pady=5)

        previous_button = tk.Button(self, text="Previous Hangs", command=lambda: controller.show_frame("PreviousHangs"))
        previous_button.pack(pady=5)
