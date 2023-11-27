# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hello {name}')
    
# Return Value
def getSum(a,b):
    return a+b

# Anonymous Fun  
sumNum = lambda a,b: a+b

# (Infinite Currying like javascript but fail!)
def infinite_curr(a):
  def curr(b):
    if b:
      return a+b
    else:
      return a
  return curr
    
  
print(sumNum(4,6))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


