import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import time
import threading
import random

class MockBluetoothSensor:
    """Simulate Bluetooth force sensor data."""
    def __init__(self, duration=10):
        self.duration = duration
        self.start_time = time.time()

    def get_force_data(self):
        """Simulate a data packet received from the force sensor."""
        if time.time() - self.start_time < self.duration:
            return random.uniform(0, 100)  # Random force data
        return None  # End simulation after the duration

class HangboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangboard Timer and Tracker")

        # Initialize Mock Bluetooth Sensor
        self.sensor = MockBluetoothSensor(duration=10)
        
        # Create plot figure and embed it in Tkinter
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

        # Set up plot
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 100)
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Force (N)")
        self.line, = self.ax.plot([], [], label="Force over Time")
        self.ax.legend()
        
        # Button to start tracking
        self.start_button = tk.Button(root, text="Start 10s Pull", command=self.start_tracking)
        self.start_button.pack()

    def start_tracking(self):
        # Reset the sensor and plot for a new session
        self.sensor = MockBluetoothSensor(duration=10)
        self.line.set_xdata([])
        self.line.set_ydata([])
        self.ax.set_xlim(0, 10)
        
        # Start tracking on a new thread
        tracking_thread = threading.Thread(target=self.plot_force_real_time)
        tracking_thread.start()

    def plot_force_real_time(self):
        # Real-time plotting logic
        x_data, y_data = [], []
        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time
            force = self.sensor.get_force_data()
            
            if force is None:  # Stop if no more data
                break

            x_data.append(elapsed_time)
            y_data.append(force)

            # Update plot data
            self.line.set_xdata(x_data)
            self.line.set_ydata(y_data)
            self.ax.set_xlim(0, max(elapsed_time, 10))
            self.canvas.draw()
            time.sleep(0.1)  # Simulate real-time delay

# Initialize Tkinter root and the app
root = tk.Tk()
app = HangboardApp(root)
root.mainloop()
