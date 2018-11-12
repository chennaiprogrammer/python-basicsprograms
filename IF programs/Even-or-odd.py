"""
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd
"""
number = int(input("enter the number:"))
"""
if number%2==0:
    print("even number",number)
else:
    print("odd number",number)
"""
status="even number"

if number%2:
    status='odd number'
print(status)



