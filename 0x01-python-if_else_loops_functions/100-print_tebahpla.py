#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    char = chr(i)

    # Toggle between lowercase and uppercase
    if char.islower():
        char = char.upper()
    else:
        char = char.lower()

    print(char, end='')

# Print a newline character to end the line
print()
