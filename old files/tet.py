import matplotlib.pyplot as plt
import numpy as np
import time

# Define the function to simulate real-time plotting of force data
def plot_force_real_time(duration=10):
    # Initialize the plot
    plt.ion()  # Interactive mode on
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    line, = ax.plot(x_data, y_data, label="Force over Time")
    ax.set_xlim(0, duration)
    ax.set_ylim(0, 100)  # Adjust the y-axis range based on expected force range
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Force (N)")
    ax.legend()
    
    # Generate and plot data for the specified duration
    start_time = time.time()
    while time.time() - start_time <= duration:
        elapsed_time = time.time() - start_time
        force = np.random.uniform(0, 100)  # Fake data: replace with sensor input later
        x_data.append(elapsed_time)
        y_data.append(force)
        
        # Update the plot data
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        ax.set_xlim(0, max(elapsed_time, duration))
        plt.draw()
        plt.pause(0.1)  # Small delay to simulate real-time plotting

    plt.ioff()  # Turn off interactive mode
    plt.show()

# Run the function to test
plot_force_real_time(duration=10)
