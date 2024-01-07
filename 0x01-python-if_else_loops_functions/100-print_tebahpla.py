#!/usr/bin/python3

print("".join(chr(i) if i % 2 else chr(i - 32) for i in range(123, 64, -1)))
