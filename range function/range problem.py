#predict the output

num=range(1,10,-1)
lst=list(num)
#lst produces empty list because start value has positive value and stop value has positive
#but jump value has negative value

num1=range(-1,-10,1)
lst1=list(num1)

print('both produce',lst,lst1,'list')

#if it is postive value produce empty list
num2=range(10,1,1)
lst2=list(num2)
print('list 2 start val>stop val',lst2)
#start value > stop value so jump value must be negative

num3=range(10,1,-1)
lst3=list(num3)
print('list 3',lst3)

num4=range(-10,1,-1)
lst4=list(num4)
print('list 4',lst4)

