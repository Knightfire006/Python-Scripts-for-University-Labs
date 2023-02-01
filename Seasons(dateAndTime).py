import datetime

"""Write a program that takes a date as input and outputs the date's season. The input is a string to represent the month and an int to represent the day.

Ex: If the input is:

April
11

the output is:

Spring

The dates for each season are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19

"""
# gets the current year to use as a variable in season variables
today = datetime.date.today()
current_year = today.year

# creates the ranges for our seasons
spring = { "Beginning": (datetime.datetime(current_year, 3, 20)), "End": (datetime.datetime(current_year, 6, 20))}
summer = { "Beginning": (datetime.datetime(current_year, 6, 21)), "End": (datetime.datetime(current_year, 9, 21))}
fall = { "Beginning": (datetime.datetime(current_year, 9, 22)), "End": (datetime.datetime(current_year, 12, 20))}
winter = { "Beginning": (datetime.datetime(current_year, 12, 20)), "End": (datetime.datetime(current_year, 6, 20))}

# takes user input for month and day
month_name = input()
day = input()

# simple try statement to check for valid month/day entries. valid_state is set to true if true else false
valid_date = False
try:
    day = int(day)
    month_num = datetime.datetime.strptime(month_name, '%B').month
    date = datetime.datetime(current_year, month_num, day)
    valid_date = True
except ValueError:
    valid_date = False

# if the user input is a valid date, then we compare it to the Beginning and ending of each season
if valid_date:

    user_date = datetime.datetime(current_year, month_num, day)
    # winter is January 1st to March 19th, and December 21st to December 31st
    if winter["End"] >= user_date < spring["Beginning"] or user_date >= winter["Beginning"]:
        print("Winter")

    # spring is March 20th to June 20th
    elif spring["Beginning"] <= user_date <= spring["End"]:
        print("Spring")

    # summer is June 21st to September 21st
    elif summer["Beginning"] <= user_date <= summer["End"]:
        print("Summer")

    # Fall/Autumn is September 22nd to December 20th
    elif fall["Beginning"] <= user_date <= fall["End"]:
        print("Autumn")
        
else:
    # if not a valid date is entered
    print("Invalid")






