from datetime import datetime
import time
import pytz
import winsound
india = pytz.timezone('Asia/Kolkata')
now = datetime.now(india)
print(now)
alarm = input("Enter the time of alarm to be set in 12 hour format-HH:MM:SS:(AM/PM)\n")
hour = alarm[0:2]
if (hour>"12"):
  hour=hour-12
else:
  hour
minute = alarm[3:5]
seconds = alarm[6:8]
period = alarm[9:11].upper()
print("alarm set..")


while True:
    now = datetime.now(india)
    hournow = now.strftime("%I")
    minutenow = now.strftime("%M")
    secondsnow = now.strftime("%S")
    periodnow = now.strftime("%p")
    print(f"Current time: {int(hournow):02d}:{int(minutenow):02d}:{int(secondsnow):02d}")
    time.sleep(1)
    if(period == periodnow):
        if(hour == hournow):
            if(minute == minutenow):
                if(seconds == secondsnow):
                    print("Wake Up!")
                    # Play sound for 2 seconds
                    winsound.Beep(1000, 2000)  # frequency = 1000Hz, duration = 2000ms
                    break
