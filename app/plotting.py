import time

class RealTimePlot:
    def __init__(self, ax):
        self.ax = ax
        self.line, = ax.plot([], [], label="Force over Time")
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 100)
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Force (N)")
        self.ax.legend()
        self.x_data = []
        self.y_data = []

    def reset_data(self):
        self.x_data = []
        self.y_data = []
        self.line.set_xdata(self.x_data)
        self.line.set_ydata(self.y_data)
        self.ax.set_xlim(0, 10)

    def plot_data(self, sensor):
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            force = sensor.get_force_data()
            
            if force is None:  # Stop if no more data
                break

            self.x_data.append(elapsed_time)
            self.y_data.append(force)

            # Update plot data
            self.line.set_xdata(self.x_data)
            self.line.set_ydata(self.y_data)
            self.ax.set_xlim(0, max(elapsed_time, 10))
            self.ax.figure.canvas.draw()
            time.sleep(0.1)  # Simulate real-time delay
