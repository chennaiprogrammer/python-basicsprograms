#predict the output
"""
AND operator has higher precedence than OR operator. So, it is evaluated first.(b and c) evaluates to false
Now OR operator is evaluated (True or False) evaluates to True. So the if condition becomes True
"""
a = True
b = False
c = False

if a or b and c:
    print("#CHENNAI PROGRAMMER#")
else:
    print("$-chennai programmer-$")
"""
a = True
b = False
c = False
  
if not a or b: 
    print 1
elif not a or not b and c: 
    print 2
elif not a or b or not b and a: 
    print 3
else: 
    print 4"""
