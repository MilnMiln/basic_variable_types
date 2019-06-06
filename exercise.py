#! /usr/bin/python3

# Floats
myFloat = 7.1

# Integers
myInt = 2
a, b = 3, 4

# Strings
myString = "This is a string."

# Tests
if isinstance(myFloat, float):
    print ("myFloat is a float-type.")

if isinstance(myInt, int):
    print ("myInt is an integer.")

if myString == "This is a string.":
    print("myString = '%s', and is therefore a string." % myString)

# Output
print ("Floats: %.2f" % myFloat, float(myInt)) # With a formatting string.

print ("Integers:", myInt, int(myFloat), a, b)

print ("Strings:", myString)
