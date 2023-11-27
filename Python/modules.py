# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core module
import datetime
from datetime import date
from time import time

# Pip module
# import camelcase
# from camelcase import CamelCase

# Import custom module 
from validator import validate_email

today1 = datetime.date.today()
today = date.today()
timestamp = time()

# c = CamelCase()

# print(c.hump('hello world '))

email = 'test@test.com'

if validate_email(email):
    print(f'{email} is vaild')
else:
    print(f'{email} is invaild')
