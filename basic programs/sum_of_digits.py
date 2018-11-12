"""
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number.
For example, if the user enters 3141 then your program should display 3+1+4+1=9.
"""
number = int(input("enter the number:"))

lst=list(str(number))
sum=0
for i in lst:
    sum = sum + eval(i)
print(sum)





