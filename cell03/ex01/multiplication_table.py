#!/usr/bin/env python3
print("Enter a number")

input = input()

num = int(input)

for i in range(10):
    print(f"{i} x {num} = {i*num}")