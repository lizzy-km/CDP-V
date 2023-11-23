# Python has functions for creating, reading, updating, and deleting files.

# Open a file

myFile = open("myfile.txt", "w")

# Get some info

print("Name: ", myFile.name)
print("Is Closed: ", myFile.closed)
print("Opening: ", myFile.mode)

# Write to file

myFile.write("I love Python")
myFile.write(" and Javascript")
myFile.close()

# Append to file

myFile = open("myfile.txt", "a")

myFile.write(" I love Lalisa")
myFile.write(" and her members")
myFile.close()

# Read from file

myFile = open("myfile.txt", "r+")
text = myFile.read(100)
print(text)
