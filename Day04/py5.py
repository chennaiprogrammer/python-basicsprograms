"""
Input:
N = 3

Output:
   *
  ***
 *****
"""
num = int(input("enter the number :"))
star = range(1,num*2,2)
sp  = range(num)[::-1]
for i in range(len(sp)):
    print(" "*sp[i] +"*"*star[i])