"""
Create a program that reads two integers, a and b, from the user.
Your program should compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of ab

"""
from math import sqrt
number1 = int(input("enter the first number:"))
number2 = int(input("enter the second number:"))

print("add number1 and number2",number1 + number2)
print("subtract number1 and number2",number1-number2)
print("multiply number1 and number2",number1*number2)
print("div number1 and number2",number1/number2)
print("sqrt",pow(number1,number2))