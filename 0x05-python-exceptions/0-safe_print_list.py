#!/usr/bin/python3

# quck project

def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError:
            break
    print()
    return(total)
