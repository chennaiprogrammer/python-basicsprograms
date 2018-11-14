#write a code to perform multiplication of two numbers
#without using multiplication operator
#using while loop
# value 1 and value 2
first_num=int(input("enetr the first number:"))
second_num=int(input("enter the second number:"))
multi=0
'''if (second_num<0):
    
    first_num=first_num+second_num
    second_num=first_num-second_num
    first_num=first_num-second_num'''


if(first_num>=0):
    cnt=1   
    while(cnt<=first_num):
          multi+=second_num
          cnt=cnt+1
if(first_num<0):
    cnt=first_num
    while(cnt<=-1):
        multi-=second_num
        cnt=cnt+1
print(multi)
