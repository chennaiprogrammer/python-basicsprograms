"""
N=5
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1

"""

N=int(input("enter the number:"))

for i in range(N,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print( )