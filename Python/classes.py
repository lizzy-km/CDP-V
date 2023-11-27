# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Contrustor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
            
    def greeting(self):
        return f'My name is {self.name} and I m {self.age} years old.'
    
    def has_birthday(self):
        self.age += 1
        

# Extend Class
class Customer(User):
    # Contrustor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        
    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} and I m {self.age} years old and my balance is $ {self.balance} million Dollor.'

# Init user object
brad = User('Brad Traversy','test@gmail.com',24)

# INit Cus Obj
jennie = Customer('Jennie Kim','jennie@gmail.com',26)

jennie.set_balance(2500)

brad.has_birthday()
print(jennie.greeting())
