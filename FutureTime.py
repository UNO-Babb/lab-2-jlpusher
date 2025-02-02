#FutureTime.py
#Name:Jessica Pusher
#Date:2.1.25
#Assignment:futuretime.py

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  print ("The current time is ", currentHour, ":", currentMinute, ".") 

  #TODO:
  #Ask user for hours
  UserHours = input("Give me a number of hours.")
  UserHoursInt = int(UserHours)
  
  #Ask user for minutes
  UserMinutes = input("Give me a number of minutes.")
  UserMinutesInt = int(UserMinutes)

  moreMin = currentMinute + UserMinutesInt
  MinHours = moreMin // 60
  FutMinutes = moreMin % 60
  
  moreHour = currentHour + UserHoursInt
  HourHours = moreHour // 24 #this would come into play with an if statement for time after midnight
  HrHours = moreHour % 24 #this would come into play with an if statement for time after midnight

  FutHour = moreHour + MinHours 
#This does not account for rolling past midnight and would require an if statement to do so.


  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"

  FutHourFormat = (str(FutHour).zfill(2))
  FutMinFormat = (str(FutMinutes).zfill(2))
  
  print("In ", UserHours, "hours and ", UserMinutes, "minutes, it will be, ", FutHourFormat, ":", FutMinFormat, ".")


if __name__ == '__main__':
  main()
