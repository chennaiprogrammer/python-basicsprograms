

name = input("enter the name:")
sp = range(len(name))

for i in range(len(name*2)):
    
    line = " "*sp[i]+name[i]
    print(line)