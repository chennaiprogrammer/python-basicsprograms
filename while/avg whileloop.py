"""
Take 10 integers from loop and print their average value on the screen

"""
start=int(input('enter the number:'))
end=int(input('enter end value:'))
print('print value from %d to %d:'%(start,end))
sum=0
while(start<end+1):
    print(str(start),',',end="")
    sum+=start
    start+=1
avg=sum/10
print("\n","total value:",sum,'average value',avg)