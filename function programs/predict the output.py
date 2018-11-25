"""The variable count declared outside the function is global variable and also the count
variable being referenced in the function is the same global variable defined outside of the
function.So, the changes made to variable in the function is reflected to the original
variable.So, the output of the program is 4.
"""
count = 1

def doThis():

    global count

    for i in (1, 2, 3):
        count += 1

doThis()

print(count)