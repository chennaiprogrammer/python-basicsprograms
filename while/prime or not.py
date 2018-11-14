#write a program to get a number from user and print if it is prime or not
num=int(input("enter the num:"))
cnt = 2
status = 0
while(cnt<num):
    if num%cnt == 0:
        status = 1
        break
    cnt += 1
if status == 0:
    print(num,"is prime")
else:
    print(num,"is not prime ")

