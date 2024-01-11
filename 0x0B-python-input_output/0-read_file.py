#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file: "" Open the file in read mode with UTF-8 encoding""
contents = file.read()
print(contents)
