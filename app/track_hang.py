import tkinter as tk

class TrackHangPage(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        tk.Label(self, text="Track Hang Session", font=("Arial", 16)).pack(pady=10)
        
        # Entry for hang time
        tk.Label(self, text="Hang Time (s):").pack()
        self.hang_time_entry = tk.Entry(self)
        self.hang_time_entry.pack()
        
        # Entry for number of sets
        tk.Label(self, text="Number of Sets:").pack()
        self.sets_entry = tk.Entry(self)
        self.sets_entry.pack()

        # Entry for rest time
        tk.Label(self, text="Rest Time (s):").pack()
        self.rest_time_entry = tk.Entry(self)
        self.rest_time_entry.pack()

        # Start tracking button
        start_button = tk.Button(self, text="Start Session", command=self.start_session)
        start_button.pack(pady=10)

        # Back to home button
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("Home"))
        back_button.pack(pady=5)

    def start_session(self):
        # Here you'd retrieve user inputs and start tracking the session
        hang_time = int(self.hang_time_entry.get())
        sets = int(self.sets_entry.get())
        rest_time = int(self.rest_time_entry.get())
        # TODO: Implement session start with these values
        print(f"Starting session with hang time {hang_time}, {sets} sets, and {rest_time} seconds rest")
