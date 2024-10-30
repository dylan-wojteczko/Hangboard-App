import tkinter as tk

class Navigation:
    def __init__(self, root):
        self.root = root
        self.frames = {}

    def add_frame(self, frame_class, name):
        """Add a new frame to the navigation system."""
        frame = frame_class(self.root, self)
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name):
        """Raise the frame to the front."""
        frame = self.frames[name]
        frame.tkraise()
