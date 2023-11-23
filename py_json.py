# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample

userJson = '{"first_name": "Kim", "last_name":"Jisoo", "age":"27" }'

# Parse to dict

user = json.loads(userJson)

print(user)
print(user['first_name'])

car ={
    'make':'Ford',
    'model':'Mustang',
    'year':1970
}

carJson = json.dumps(car)

print(carJson)