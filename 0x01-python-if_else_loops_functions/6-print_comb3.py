#!/usr/bin/python3

for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit != 9 or ones_digit != 9:
            print("{:02d}, ".format(10 * tens_digit + ones_digit), end="")

# Print a newline at the end
print()
