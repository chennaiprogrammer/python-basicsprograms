s="Suresha"
"""
for i in range(len(s)):
    for j in range(len(s)):
        if i == j:
            print(s[i], end="")
        
        print(" ", end="")
    print()
"""
middle = int(len(s)/2)+1
fp = s[:middle]
l = []
for i in range(len(fp)):
    l.append([i+1, fp[i]] )
print(l)
lines = []
for i in l:
    line = [ '' for j in range(len(s)) ] 
    line[i[0]-1] = i[1]
    line[-i[0]] = i[1]
    lines.append(line)
print(lines)


sp = s[middle:]
l2 = []
for i in range(len(sp)):
    l2.append([i+1, sp[i]])
    line = [ '' for j in range(len(s)) ]
    line[len(fp)-1-(i+1)] = sp[i]
    line[len(fp)-1 + (i+1)] = sp[i]
    lines.append(line)
ls = []
for i in lines:
    l = " ".join(i)
    ls.append(l)
print("\n".join(ls))
    


    
    