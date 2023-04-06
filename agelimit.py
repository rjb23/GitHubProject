# lets create a simple script to print out the current date and time
# import the datetime module
import datetime
# use the datetime module to get the current date and time
now = datetime.datetime.now()
# print the current date and time
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# now lets ask the user for their birthday
# and print out how many days until their birthday
# import the datetime module
# use the datetime module to get the current date and time
now = datetime.datetime.now()
# get the current year
year = now.strftime("%Y")
# get the current month
month = now.strftime("%m")
# get the current day
day = now.strftime("%d")
# get the current hour
hour = now.strftime("%H")
# get the current minute
minute = now.strftime("%M")
# get the current second
second = now.strftime("%S")
# get the current microsecond
microsecond = now.strftime("%f")
# get the current date and time
current_date = datetime.datetime(int(year), int(month), int(
    day), int(hour), int(minute), int(second), int(microsecond))
# get the user to enter their birthday
birthday = input("Please enter your birthday in the format YYYY-MM-DD : ")
# split the birthday into year, month and day
year, month, day = birthday.split("-")
# create a date object from the birthday
birthday_date = datetime.datetime(int(year), int(month), int(day), 0, 0, 0, 0)
# get the difference between the current date and time and the birthday
difference = birthday_date - current_date
# print the difference
print("Number of days until your birthday : " + str(difference.days))
