""""
N=5
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1


"""
N=int(input("enter the number:" ))

for i in  range(N,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print( )
