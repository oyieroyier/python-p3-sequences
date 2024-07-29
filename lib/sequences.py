#!/usr/bin/env python3

def print_fibonacci(length):
    arr = []

    for i in range(length):
        arr.insert(len(arr), (arr[-1]) + (arr[-2]) if len(arr) > 1 else i)
    print(arr)

print_fibonacci(9)


