"""
input  start value and stop value find prime number in it
"""
start_value=int(input("enter the start value:"))
stop_value=int(input("enter the stop value:"))

for i in range(start_value,stop_value+1):

    if i>1:
        for num in range(2,i):
            if  i%num==0:
               break
            else:
               print(i,'prime number')
