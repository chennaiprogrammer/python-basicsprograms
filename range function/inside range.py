"""
behind scenes of range function
create of function next chapter
"""
def Range(*args):
    lst=[]
    if len(args)==0 :
        print('need stop value')
    elif len(args)==1:
        start=0
        jump=1
        while(start<args[0]):
            lst.append(start)
            start+=jump
            return lst
    elif len(args)==3:
        start,stop=args
        jump=1
        while(start<stop):
            lst.append(start)
            start+=jump
            return lst
    else:
        print("invalid data")
