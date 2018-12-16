

"""
 Write a program to get name and age of 10 people and store it in a dictionary then
 print the dictionary and try same and unique values
"""


NameBook = {}
for i in range(10):

    Name = input("enter the name :")
    AGE = int(input("enter the age :"))
    NameBook[Name] = [AGE]
print(NameBook)





