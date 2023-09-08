#!/usr/bin/python3

# Assign values to variables a and b
a = 1
b = 2

from add_0 import add

# Calculate the result using the imported add function
result = add(a, b)

# Check if this script is the main program
if __name__ == "__main__":
    # Print the result using string formatting
    print("{} + {} = {}".format(a, b, result))
