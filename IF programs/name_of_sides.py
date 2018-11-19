"""
Write a program that determines the name of a shape from its number of sides.Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
"""

sides=int(input("enter the number of sides(3 to 10):"))

name=""
if sides==3:
    print("triangle")
elif sides ==4:
    print("quadrilateral")
elif sides == 5:
    print("pentagon")
elif sides == 6:
    print("hexagon")
elif sides == 7:
    print("heptagon")
elif sides == 8:
    print("octagon")
elif sides == 9:
    print("nonagon")
elif sides == 10:
    print("decagon")

if name=="":
    print("error message not more than 10 slides")