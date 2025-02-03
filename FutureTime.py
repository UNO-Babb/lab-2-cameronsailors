#FutureTime.py
#Name: Cameron Sailors
#Date: 2/2/2025
#Assignment: FutureTime

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print("The current time is " + f"{currentHour}:{currentMinute}")

  #TODO:
  #Ask user for hours
  addedHours=int(input("Enter number of hours to pass: "))
  
  #Ask user for minutes
  addedMinutes=int(input("Enter number of minutes to pass: "))

  #Calculate the time after the user-supplied time has passed.
  totalMinutes = currentMinute + addedMinutes

  extraHours = totalMinutes // 60
  newMinutes = totalMinutes % 60

  totalHours = currentHour + addedHours + extraHours 

  newHours = ((totalHours -1)% 12)+1

  #Output the future time in standard format "HH:MM"

  print("The future time is: " + f"{newHours}:{newMinutes}")

if __name__ == '__main__':
  main()
