"""
write student details in file using dictionary be careful while calling function and passing values
file in append mode
"""

def student_details(ID,NAME,AGE,college_name,year_of_passing):
    details={}
    if ID not in details:
        details[ID]=[NAME,AGE,college_name,year_of_passing]
    file=open('details.txt','a')
    file.write(str(details))
student_details(1,'suresh',21,'anna univ',2018)