"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest and vice versa). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.

"""

first_num =int(input("enter the first number:"))
second_num=int(input("enter the second number:"))
third_num=int(input("enter the third number"))

large = max(first_num,second_num,third_num)
small = min(first_num,second_num,third_num)

total = first_num+second_num+third_num
middle = total-(large+small)

print("desending order:",large,middle,small,)
print("ascending order:",small,middle,large)