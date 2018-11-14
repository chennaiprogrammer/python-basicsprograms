# write program to get number and to print 'prime' based on input 



number=int(input("enter the number"))
STATUS="PRIME"
limit = int(number/2) + 1

for i in range(2, limit):
    if number%i==0:
        STATUS="Not Prime"
        break
    print(i)
    
print(STATUS)

