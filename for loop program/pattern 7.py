"""
N=5
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

"""

N=5#int(input("enter the number:"))
space = range(N+1)[::-1]
j=0
for i in range(1,N*2,2):
     print(" "*space[j]+"*"*i)
     j+=1
