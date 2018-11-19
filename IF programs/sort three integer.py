"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest and vice versa).only using if condition statments

"""

# Get user input
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

small = 0
middle = 0
large = 0

# IF Statement

# large
if first >= third and first >= second:
    large = first
    if second > third :
        middle = second
        small=third
    else:
        middle = third
        small=second

# MIDDLE
elif second > first and second > third:
    large = second
    if first > third:
        middle = first
        small=third
    else:
        middle = third
        small =first

# LARGE
elif third > second and third > first :

    large = third
    if second > first:
        middle = second
        small=first
    else:
        middle = first
        small=second

# Display Results
print("The numbers in accending order are: ", small, middle, large)