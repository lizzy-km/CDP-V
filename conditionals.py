# If/ Else conditions are used to decide to do something based on something being true or false

x = 3
y = 19
true = True
false = False


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple If else
if x > y:
    print(f"{x} is greater than {y}")
elif x == y:
  print(f"{x} is equal to {y}")
else:
    print(f"{x} is less than {y}")

# Nested if

if x > 2 :
    if x <= 10:
      print(f'{x} is greater than 2 and less than or equal to 10')
  

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
  print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:
  print(f'{x} is greater than 2 or less than or equal to 10')

# not
if not(x == y):
    if x > 2 and x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5,6,7]

# in
if x in numbers:
    print(true)

# not in
if y not in numbers:
    print(false) 

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
    print(true)
else:
    print(false)  

# is not
if x is not y:
    print(true)
else:
    print(false)  
