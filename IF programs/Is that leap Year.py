"""
Write a program that reads a year from the user and displays a message indicating
whether or not it is a leap year.Any year that is divisible by 400 is a leap year.
• Of the remaining years, any year that is divisible by 100 is not a leap year.
• Of the remaining years, any year that is divisible by 4 is a leap year.
• All other years are not leap year
"""

year=int(input("enter the year:"))

if year%400==0:
    leap_year=True
elif year%100==0:
    leap_year=False
elif year%4==0:
    leap_year=True
else:
    leap_year=False

if leap_year:
    print(year,"is leap year")
else:
    print(year,"is not leap year")