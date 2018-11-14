#Write a code to relocate the positions of even numbers to left in a list
"""
Enter a list: [ 2,55,4,6,7,9,19,8 ]
Reordered list is [ 2, 4, 6, 8, 55, 7, 9, 19 ]
"""
numbers=eval(input("enter the list:"))
even,odd=[],[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        

print(even+odd)
