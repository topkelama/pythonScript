#!/usr/bin/python3
import sys
#a simple user interactive python script

balance_info = {'Tom':23000,'Nancy': 120050, 'Nick':2400,'Kalpana':2500}
name = input("Enter your name: ")
name = name.capitalize()
if not name in balance_info:
    print("user %s does not exist in the system. "%(name))
    sys.exit(1)
else:
    print("Welcome to My bank")
balance = balance_info[name]
if balance < 0:
    print("Your account is terminating soon! ")
elif balance == 1500:
    print("your balance %d,it is low balance "%(balance))
else:
    print("your current balance is %d" %(balance))
print("Thank you..")

