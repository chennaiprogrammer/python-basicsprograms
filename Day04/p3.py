


name=input("enter the name :")
rev=range(len(name))[::-1]
lines = []
for i in range(len(name)):
    line = [' ']*len(name)
    line[0] = name[i]
    line[-1] = name[-(i+1)]
    lines.append(line)
print(lines)
lines[-1] = list(name)[::-1]
print(lines)

for i in lines:
    print("".join(i))