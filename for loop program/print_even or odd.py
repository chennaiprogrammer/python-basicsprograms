
"""
input start value and stop value to find even and odd number between them
"""
start_value=int(input("enter the start value:"))
stop_value=int(input("enter the stop value:"))

for i in range(start_value,stop_value+1):
    if i%2==0:
        print("even number",i)
    else:
        print("odd number",i)