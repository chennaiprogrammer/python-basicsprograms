"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using the formula:
sum = (n(n + 1))/2
"""
number = int(input("enter the postive integer:"))

Sum = int((number*(number + 1))/2)

print("sum of first", number, "postive integer", Sum)

