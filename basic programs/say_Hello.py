
#Write a program that asks the user to enter his or her name and age of person.
#The program should respond with a message that says hello to the user, using his or her name.
#identify person major or minor

# input method use to get input from user as string
Name = input("enter the name of person:")
#age get value as integer number using input get input as string   
age = int(input("enter the age of person:"))

print("hello",Name)

if age < 18 :
    print("person is minor")
else:
    print("person is major")