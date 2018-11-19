"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.
"""
side1=float(input("enter the side1:"))
side2=float(input("enter the side2:"))
side3=float(input("enter the side3:"))

if side1==side2==side3:
    print("equilateral triangle")
elif side1==side2 or side2==side3 or side1==side3:
    print('isosceles triangle')
else:
    print('scalene trinagle')