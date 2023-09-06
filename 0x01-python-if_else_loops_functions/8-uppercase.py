#!/usr/bin/python3
def uppercase(input_str):
    result = ""
    for char in input_str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert it to uppercase using ord() and chr()
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            result += char  # Keep non-lowercase characters unchanged
    print(result)
