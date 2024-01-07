#!/usr/bin/python3

# Initialize an empty string to store the result
result = ""

# Iterate over the range from 122 to 65 (inclusive) in reverse order
for i in range(122, 64, -1):
    # Add the character to the result string based on the conditions
    result += chr(i) if i % 2 == 0 else chr(i - 32)

# Print the result without a newline at the end
print(result, end="")
