

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):

    if b==0:
        raise ValueError("hey, b value is zero so cannot be divided by zero")
    return a/b
