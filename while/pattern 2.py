"""
  *
 ***
*****
"""
num=int(input('enter the number:'))
i=1
space=num-1
while(i<num*2):
        print(' '*space+'*'*i)
        space-=1
        i+=2