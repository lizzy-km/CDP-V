# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

BlackPink = [
    {"id": "0", "name": "Lalisa"},
    {"id": "1", "name": "Jennie Kim"},
    {"id": "2", "name": "Kim Jisoo"},
    {"id": "3", "name": "Park Chaeyoung"},
]

# break
for members in BlackPink:
    if members.get("name") == "Kim Jisoo":
        break
    print("# Break", members.get("id"))

# continue (Skip)
for members in BlackPink:
    if members.get("name") == "Kim Jisoo":
        continue
    print("# Continue", members.get("id"), members.get("name"))


# range
for i in range(len(BlackPink)):
    print("# Range", BlackPink[i].get("id"), BlackPink[i].get("name"))

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
