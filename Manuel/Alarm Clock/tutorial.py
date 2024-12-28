import datetime

birthday = datetime.datetime(2025, 5,5)

print(birthday)

print(birthday.date())
print(birthday.weekday())
print(birthday.strftime("%A"))

print(datetime.datetime.now())
