import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pytz

# Set the time zone to Asia/Kolkata
india = pytz.timezone('Asia/Kolkata')


def update_time():
  current_time = datetime.now(india).strftime(time_format.get())
  label.config(text=current_time)
  label.after(1000, update_time)  # Update every 1000ms (1 second)
  check_alarm(current_time)  # Check if it's time for the alarm

def set_alarm():
  alarm_time_str = alarm_time.get()
  alarm_datetime = datetime.strptime(alarm_time_str, '%H:%M:%S')
  alarm_hour = alarm_datetime.hour
  alarm_minute = alarm_datetime.minute
  alarm_second = alarm_datetime.second
  alarm_active.set(True)
  alarm_label.config(text=f"Alarm set for: {alarm_time_str}")


def check_alarm(current_time):
  if alarm_active.get() and alarm_time.get() == current_time:
    messagebox.showinfo("Alarm", "Time's up! Wake up!")

    #audio.stop_source(source)


# Create the main window
root = tk.Tk()
root.title("Digital Clock with Alarm")
root.geometry("400x350")
root.configure(bg="#2C3C3F")  # Set background color

# Create a frame for time display, radio buttons, and alarm
frame = tk.Frame(root, bg="#2C3C3F")
frame.place(relx=0.5, rely=0.3, anchor="center")

# Create a label to display the time
label = tk.Label(frame,
                 text="",
                 font=("Arial", 48),
                 bg="#2C3C3F",
                 fg="#00D2FF")
label.pack()

# Create a StringVar to hold the selected time format
time_format = tk.StringVar()
time_format.set('%H:%M:%S')  # Default to 24-hour format

# ... (Rest of your code for radio buttons and time format)

# Create an entry for setting the alarm time
alarm_time = tk.StringVar()
alarm_entry = tk.Entry(root, textvariable=alarm_time, font=("Arial", 16))
alarm_entry.place(relx=0.5, rely=0.5, anchor="center")

# Create a button to set the alarm
set_alarm_button = tk.Button(root, text="Set Alarm Time", command=set_alarm)
set_alarm_button.place(relx=0.5, rely=0.7, anchor="center")

# Create a StringVar to hold the alarm status
alarm_active = tk.BooleanVar()
alarm_active.set(False)

# Create a label to display the alarm status
alarm_label = tk.Label(root, text="", font=("Arial", 12))
alarm_label.place(relx=0.5, rely=0.8, anchor="center")

# Start updating the time
update_time()

# Start the Tkinter main loop
root.mainloop()
