#! /usr/bin/python3

# Floats
myFloat = 7.1

# Integers
myInt = 2
a, b = 3, 4

# Strings
myString = "This is a string."

if isinstance(myFloat, float):
    print ("myFloat is a float-type.")

if isinstance(myInt, int):
    print ("myInt is an integer.")

print ("Floats: %f, " % myFloat, float(myInt)) 

print ("Integers: ", myInt, int(myFloat), a, b)

print ("Strings: ", myString)
