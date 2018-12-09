"""
N=5
   1
   22
   333
   4444
   55555

"""
N=int(input("enter the integer:"))

for i in range(N+1):
    print(str(i)*i)