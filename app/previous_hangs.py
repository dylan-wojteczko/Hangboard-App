import tkinter as tk

class PreviousHangsPage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        tk.Label(self, text="Previous Hangs", font=("Arial", 16)).pack(pady=10)

        # Placeholder for past sessions list
        self.session_listbox = tk.Listbox(self)
        self.session_listbox.pack(pady=5)

        # Back to home button
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("Home"))
        back_button.pack(pady=5)

        # Populate with mock data
        self.populate_sessions()

    def populate_sessions(self):
        # TODO: Replace this with actual session loading
        for i in range(1, 6):
            self.session_listbox.insert(tk.END, f"Session {i} - 2024-10-{i+20}")
