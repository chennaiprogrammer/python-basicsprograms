
"""create dictionary and access key  and value"""

Zoo_animals = {}

Zoo_animals[1]='lion'
Zoo_animals[2]='Tiger'
Zoo_animals[3]='Monkey'
Zoo_animals[4]='horses'
Zoo_animals[5]='elphants'
Zoo_animals[6]='bears'

print(Zoo_animals)

#access keys in dictionary
print(1,Zoo_animals.keys())

#access values in dictionary

print(2,Zoo_animals.values())

#access values using keys
print(Zoo_animals[1])

#access key by default iterating dictionary
for i in Zoo_animals:
    print('accessing key :',i)
#acess values by using funtion get(key) return value
for i in Zoo_animals:
    print('values in dictionary',Zoo_animals.get(i))

#in this time we need access both key and values using items() with no arguments and reteun as tuples

for  i in Zoo_animals.items():
    print('access both key and values',i,type(i))
#another way access items in dictionary using items() function
for key , values in Zoo_animals.items():
    print(key," ",values,type(values))