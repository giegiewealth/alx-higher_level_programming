#!/usr/bin/python3

toggle = False

for i in range(ord('z'), ord('A') - 1, -1):
    char = chr(i)

    if toggle:
        char = char.swapcase()

    print(char, end='')

    toggle = not toggle

# Print a newline character to end the line
print()
