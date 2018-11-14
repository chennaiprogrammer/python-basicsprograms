



Name=input("enter the name :")
for i in range(len(Name)):
    line = [" "]*(len(Name)*2-1)
    line[i] =Name[i]
    line[-(i+1)] = Name[i]
    line = "".join(line)
    print(line)