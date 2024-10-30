# Hangboard Timer and Tracker

This is a desktop app for tracking force over time for hangboard training, allowing climbers to measure their pulling force in real time.

## Features
- Real-time graph of force over time
- Options for timed pulls
- Mock sensor data (to be replaced by Bluetooth sensor)

## Installation
1. Clone the repository.
2. Install dependencies with:
   ```bash
   pip install -r requirements.txt



hangboard_app/
├── main.py                 # Entry point for running the app
├── app/
│   ├── __init__.py         # Makes 'app' a package; keeps code organized
│   ├── gui.py              # Tkinter GUI setup and main app logic
│   ├── plotting.py         # Code to handle real-time plotting with matplotlib
│   └── sensor.py           # Code for Bluetooth sensor or mock sensor data
├── assets/
│   ├── icons/              # Any icons or images for the app (optional)
│   └── styles.css          # Style sheets or themes for the GUI (optional)
├── requirements.txt        # List of required packages (for `pip install -r requirements.txt`)
├── README.md               # Documentation on setting up and running the app
└── setup.py                # Setup script for packaging the app (for distribution)
