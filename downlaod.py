#! usr/bin/python3

import os

import requests

url = 'https://www.python.org/static/img/python-logo@2x.png'

myfile = requests.get(url)

open('/home/ec2-user/myTaskAutomation/pythonScript/PythonImage.png', 'wb').write(myfile.content)



