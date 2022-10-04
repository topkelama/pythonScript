#!/usr/bin/python3

#simple script that checks user validation
name = input("Please, enter your name: ")

age = int(input ("Please, enter your age: "))

if age < 5:
    print("Hello, %s, You are an infant"% name)
elif age <18:
    print("Hello, %s, You are minor" % name)
elif age< 60:
    print("Hello, %s, Your age is %d" %(name, age))
else:
    print("Hello %s, your age is %d" %(name, age))
print("Bye")
