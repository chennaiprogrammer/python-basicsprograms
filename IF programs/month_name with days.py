"""
The length of a month varies from 28 to 31 days. you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display '28 or 29 days'
for February so that leap years are addressed.
"""
month_name=input("enter the month:")
days = 31
if month_name=='April' or month_name=='June' or month_name=='September' or month_name=='November':
    days=30
elif month_name=='febuary':
    days = "days ='28' or '29'"


print(month_name,'has',days,'days')


