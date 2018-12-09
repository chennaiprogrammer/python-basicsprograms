"""
n=5
  5! =5*4*3*2*1
  5!=120
"""
N=int(input("enter the number:"))

fact=1
for i in range(1,N+1):
    fact*=i
print(fact)