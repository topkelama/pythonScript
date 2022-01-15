#!usr/bin/python3
import os
i = 1
#This code will create 4 directories with suffix 1,2,3, and 4 
#follwing "mydir"
#Make sure to provide appropriate path, if program fails to create #directories then it will throw amessage
path ="/home/ec2-user/pythonDirs/"
try:
    while i<5:
        os.mkdir(path+"mydir"+str(i))
        i+=1
except OSError:
    print("Failed to create directories!!")
