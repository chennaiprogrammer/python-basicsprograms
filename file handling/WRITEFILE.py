
"""
write data into file  and data should contain file creation time in it
write function takes one argument and only string datatype convert them into string function
"""
import datetime

file=open('datefile.txt','w')
cal = datetime.datetime.now()
x=str(cal.year)+'/'+str(cal.day)+'/'+str(cal.month)
file.write('file created on this time: '+x)

file.close()
