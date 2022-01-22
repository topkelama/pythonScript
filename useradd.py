#!usr/bin/python3

#this scrip will add a user in the linux machine
import os
import subprocess
import sys
import getpass
  
# add user function
def add_user():
  
     # Ask user to provide the user name
     username = input("Enter Username ")   
  
     # Let user input password
     password = getpass.getpass()   
         
     try:
         # executing useradd command using subprocess module
         subprocess.run(['sudo useradd', '-p', password, username ])      
     except:
         print("Failed to add user.")                     
         sys.exit(1)
# involk the function
add_user()
