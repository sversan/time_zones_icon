import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

# Define the list of time zones you want to display
TIMEZONES = [
    'UTC', 'US/Eastern', 'US/Central', 'US/Mountain', 'US/Pacific',
    'Europe/London', 'Europe/Paris', 'Asia/Tokyo', 'Australia/Sydney'
]

# Function to update the time in each time zone
def update_time():
    for tz, label in timezone_labels.items():
        tz_time = datetime.now(pytz.timezone(tz))
        label.config(text=tz_time.strftime('%Y-%m-%d %H:%M:%S'))
    root.after(1000, update_time)  # Update every second

# Create the main application window
root = tk.Tk()
root.title("Time Zone Clock")

# Dictionary to store labels for each time zone
timezone_labels = {}

# Create a frame for the time zone labels
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Populate the frame with time zone labels
for idx, tz in enumerate(TIMEZONES):
    ttk.Label(frame, text=tz, font=('Arial', 12)).grid(column=0, row=idx, sticky=tk.W)
    timezone_label = ttk.Label(frame, text='', font=('Arial', 12))
    timezone_label.grid(column=1, row=idx, sticky=tk.W)
    timezone_labels[tz] = timezone_label

# Update the time labels
update_time()

# Run the application
root.mainloop()
