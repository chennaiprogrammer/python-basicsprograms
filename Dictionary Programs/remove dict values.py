

"""
Write a program to delete all elements of a dictionary using while loop
use built-in functions of dictionary"""

d = {1:'any',2:'words',3:'with',4:'collection',5:'of',6:'character',7:'is',8:'strings'}

print(d)
    # this will cause an error because "this dictionary" no longer exists.
del d

dict = {1:'any',2:'words',3:'with',4:'collection',5:'of',6:'character',7:'is',8:'strings'}
#empty dictionary
#dict.clear()
print(dict)

dict_backup=dict.copy()
print(dict_backup)

#pop() function passes args as key to remove in dictionary
dict.pop(3)
print(dict)

#popitem() function default remove last inserted key-value pair takes no args
dict_backup.popitem()
print(dict_backup)
