#!/usr/bin/env python3

# Note: This script requires Python 3.12.7

a = 4287
b = 9006

sum_odd = 0

for x in range(a, b + 1):
    if x % 2 == 1:
        sum_odd = sum_odd + x
    else:
        continue

print(sum_odd)