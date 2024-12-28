# Let's learn about DateTime and String Indexing! 🎓

# -------- Part 1: DateTime Module Examples --------
from datetime import datetime
import pytz  # This helps us work with different time zones

print("\n--- Basic DateTime Operations ---")
# Get current date and time
current_time = datetime.now()
print(f"Current Date and Time: {current_time}")

# Get individual parts of the date/time
print(f"Year: {current_time.year}")
print(f"Month: {current_time.month}")
print(f"Day: {current_time.day}")
print(f"Hour: {current_time.hour}")
print(f"Minute: {current_time.minute}")
print(f"Second: {current_time.second}")

print("\n--- Formatting Dates and Times ---")
# DateTime Format Codes:
# %H - Hour (24-hour clock) as a zero-padded number [00-23]
# %I - Hour (12-hour clock) as a zero-padded number [01-12]
# %M - Minute as a zero-padded number [00-59]
# %S - Second as a zero-padded number [00-59]
# %p - Locale's equivalent of either AM or PM
# %d - Day of the month as a zero-padded number [01-31]
# %m - Month as a zero-padded number [01-12]
# %Y - Year with century as a decimal number [2024]
# %b - Month as locale's abbreviated name [Jan, Feb, ...]
# %B - Month as locale's full name [January, February, ...]
# %a - Weekday as locale's abbreviated name [Sun, Mon, ...]
# %A - Weekday as locale's full name [Sunday, Monday, ...]

# Different ways to format time
print(f"24-hour format: {current_time.strftime('%H:%M:%S')}")  # Example: 23:59:59
print(f"12-hour format: {current_time.strftime('%I:%M:%S %p')}")  # Example: 11:59:59 PM
print(f"Full date: {current_time.strftime('%d/%m/%Y')}")  # Example: 24/11/2024

# More format examples (commented out, but you can try them!)
# print(f"Date with month name: {current_time.strftime('%d %B %Y')}")  # Example: 24 November 2024
# print(f"Short date: {current_time.strftime('%d-%b-%y')}")  # Example: 24-Nov-24
# print(f"Day of week: {current_time.strftime('%A')}")  # Example: Sunday
# print(f"Date and time: {current_time.strftime('%d/%m/%Y %I:%M %p')}")  # Example: 24/11/2024 11:59 PM
# print(f"Custom format: {current_time.strftime('Today is %A, %B %d, %Y')}")  # Example: Today is Sunday, November 24, 2024

print("\n--- Working with Time Zones ---")
# Let's see times in different countries!
india_tz = pytz.timezone('Asia/Kolkata')
usa_tz = pytz.timezone('America/New_York')
japan_tz = pytz.timezone('Asia/Tokyo')

# Common timezone examples (commented out, but you can try them!):
# uk_tz = pytz.timezone('Europe/London')
# australia_tz = pytz.timezone('Australia/Sydney')
# dubai_tz = pytz.timezone('Asia/Dubai')
# singapore_tz = pytz.timezone('Asia/Singapore')

india_time = datetime.now(india_tz)
usa_time = datetime.now(usa_tz)
japan_time = datetime.now(japan_tz)

print(f"Time in India: {india_time.strftime('%I:%M %p')}")  # Shows hour:minute AM/PM
print(f"Time in New York: {usa_time.strftime('%I:%M %p')}")
print(f"Time in Japan: {japan_time.strftime('%I:%M %p')}")

# -------- Part 2: String Indexing Examples --------
print("\n--- String Indexing ---")
# Let's use a time string to learn indexing
time_string = "06:30:45 PM"
print(f"Our time string is: {time_string}")

# Getting individual parts using indexing
print("\nBasic Indexing:")
print(f"First character: time_string[0] = '{time_string[0]}'")
print(f"Second character: time_string[1] = '{time_string[1]}'")
print(f"Last character: time_string[-1] = '{time_string[-1]}'")

print("\nSlicing (getting multiple characters):")
print(f"Hours: time_string[0:2] = '{time_string[0:2]}'")
print(f"Minutes: time_string[3:5] = '{time_string[3:5]}'")
print(f"Seconds: time_string[6:8] = '{time_string[6:8]}'")
print(f"AM/PM: time_string[9:11] = '{time_string[9:11]}'")

# Fun examples with a sentence
print("\n--- More String Indexing Examples ---")
sentence = "Python is fun!"
print(f"Our sentence is: {sentence}")
print(f"First word: sentence[0:6] = '{sentence[0:6]}'")
print(f"Last word: sentence[-4:] = '{sentence[-4:]}'")
print(f"Every second character: sentence[::2] = '{sentence[::2]}'")
print(f"Reverse the string: sentence[::-1] = '{sentence[::-1]}'")

# -------- Part 3: Practice Time! --------
print("\n--- Try These Exercises! ---")
# Exercise 1: Get today's date in DD-MM-YYYY format
# Your code here: current_time.strftime('%d-%m-%Y')

# Exercise 2: Extract the hour from "09:15:30 AM"
# Your code here: "09:15:30 AM"[0:2]

# Exercise 3: Get the current time in your local timezone
# Your code here: datetime.now().strftime('%I:%M %p')

"""
Fun Facts about DateTime! 🌟
1. Computers store time in seconds since January 1, 1970 (called Unix timestamp)
2. DateTime helps us work with dates in a way humans can understand
3. Different countries have different time zones, that's why we use pytz!

Fun Facts about String Indexing! 📚
1. In Python, we start counting from 0, not 1
2. Negative indexes count from the end of the string
3. Slicing format is [start:end:step]
4. If you leave out the start, it begins from the start of the string
5. If you leave out the end, it goes until the end of the string
"""
