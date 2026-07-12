""""Python DateTime module is used to work with date and time in Python. It provides classes for manipulating dates and times in both simple and complex ways. The datetime module allows you to create, manipulate, and format date and time objects."""

# Datetime now()
from datetime import datetime
#import pytz

todays_time = datetime.now()
print(str(todays_time))
print(todays_time)

print("The hour is:", todays_time.hour)
# print(todays_time.day)

# Python DateTime Format
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
# print(todays_time.strftime('Today is %A and time is %H:%M:%S'))
# print(todays_time.strftime('Today is %B %d, %Y and time is %H:%M:%S'))


#Python Compare DateTime
# date and time in yyyy/mm/dd hh:mm:ss format

open_day = datetime(2024, 6, 1, 10, 30, 0)
close_day = datetime(2024, 6, 1, 18, 30, 0)

if open_day  >  close_day:
    message = "The store is open."
else:
    message = "The store is closed."
    print(message)

# Convert String to Datetime object in Python
# date and time in yyyy/mm/dd hh:mm:ss format

service = datetime.fromisoformat("2024-10-01 10:30:00")

print(service.strftime('%Y'))
print(service.strftime('%m'))
print(service.strftime('%d'))
print(service.strftime('%B'))

# Get numbers of days between 2 dates
# date and time in yyyy/mm/dd hh:mm:ss format
today_date = datetime.now()
future_date = datetime(2026, 7, 17)
days_difference = future_date - today_date
print(f'Days difference is : {days_difference.days}')