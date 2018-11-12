"""
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
"""
from math import pi

radius=float(input("enter the radius:"))

area = (pi)*radius**2
print("area=",area)
"""
pi = 2.47

r=int(input("enter the radii:"))

area=pi*r**2
print(area)
"""""
