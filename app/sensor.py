import random
import time

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
