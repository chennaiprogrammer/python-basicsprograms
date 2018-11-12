"""
Write a program that asks the user to enter the width and length of a room.
Once the values have been read, your program should compute and display the area of the
room.
The length and the width will be entered as floating point numbers.
Include units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""
width = float(input("enter the width of room:"))
length = float(input("enter the length of room:"))

area = length * width

print("are of room",area,"sq ft")




