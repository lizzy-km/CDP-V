# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1          #init
# y = 1.5        #float
# name = 'Vince' #string
true = True    #bool
# is_Cold = true

#Multiple assignment
x,y,name,is_Cold = (1,1.5,'Vince',true)

# Basic Math 
a = x+y

# Casting 
y = int(y)
z = float(y)


print(type(z), z)
