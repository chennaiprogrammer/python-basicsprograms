"""try all given logic values below"""
print('enter 1,0,None,empty(list,tuple,dictionary) and boolean value')
value=eval(input('enter the value:'))
if(value):
    status='true'
else:
    status='false'

print(status)