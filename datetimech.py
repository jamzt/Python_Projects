import sqlite3
import datetime
import pytz
now_portland = datetime.now()
print(now_portland.strftime("%Z"))
format = "%Y-%m-%d %H:%M:%S %Z%z"
 
 
portland_tz = pytz.timezone('Portland')  
nyc_tz = pytz.timezone('NYC') 
london_tz = pytz.timezone('London') 


portland = datetime.now(portland_tz)
nyc = datetime.now(nyc_tz)
london = datetime.now(london_tz)

# Define branch hours
branch_hours_start = datetime.strptime("09:00", "%H:%M")
branch_hours_end = datetime.strptime("17:00", "%H:%M")

def is_branch_open(current_time, start_time, end_time):
    return start_time <= current_time <= end_time

# Print the status for each branch
    if is_branch_open(portland, branch_hours_start, branch_hours_end):
        print("Portland Branch is open")
    else:
        print("Portland Branch is closed")

    if is_branch_open(nyc, branch_hours_start, branch_hours_end):
        print("NYC Branch is open")
    else:
        print("NYC Branch is closed")

    if is_branch_open(london, branch_hours_start, branch_hours_end):
        print("London Branch is open")
    else:
        print("London Branch is closed")
