
"""
copy data from one file to another file
readlines()- create list with values
"""

file=open('test .txt','r')

filecopy=open('backup.txt','a')

filelist = file.readlines()

print(filelist,len(filelist))

for i in filelist:
    filecopy.write(i)


