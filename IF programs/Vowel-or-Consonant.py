"""
 create a program that reads a letter of the string from the user.
 If the user enters a, e, i, o , u then your program should display a message
indicating that the entered letter is a vowel Otherwise your program should display a message indicating that the
letter is a consonant.
"""
string = input("enter the string:")

if string=='a' or string=='e' or  string =='i' or string=='o' or string=='u':
    print("vowel",string)
else:
    print("consonant")





