"""
 to create dictionary
"""
d={}

d['name']='suresh'
d['age']=21
d['gender']='male'
print(d)

"""suppose we want to insert another values in name key"""

d['name']= 'chennaiprog'
print(d)

" insert another value in name key but not to overwrite in it "

d['name'] = ['suresh','chennaiprogs','pythoninsta']
print(d)
"""to create dictionary constructor """
for i in range(3):
    NAME=[]
    AGE=[]
    Name=input('enter the name:')
    Age=int(input('enter the age:'))
    NAME.append(Name)
    AGE.append(Age)

student = dict(name=NAME,age=AGE,year=2018)
print(student)