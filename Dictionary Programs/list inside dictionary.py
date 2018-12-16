
#create list inside dictionary appending values to list
simple_dictionary = {}

simple_dictionary['student1']=[]
simple_dictionary['student1'].append('suresh')
simple_dictionary['student1'].append(21)
simple_dictionary['student1'].append(2018)
simple_dictionary['student1'].append('male')

simple_dictionary['student2']=[]
simple_dictionary['student2'].append('chennai progs')
simple_dictionary['student2'].append(21)
simple_dictionary['student2'].append(2018)
simple_dictionary['student2'].append('male')

#=========METHOD-2=========
lst=['test',21,2018,'NONE']
simple_dictionary['student3']=lst

#print(simple_dictionary)

form =('NAME','AGE','YEAR')

biodata = simple_dictionary.fromkeys(form,'test')
print(simple_dictionary)
print(biodata)






