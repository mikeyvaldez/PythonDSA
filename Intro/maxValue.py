#!/usr/bin/env python3

## MAX VALUE ##

# Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.
# Solve this without using any built-in list methods.
# You can assume that the list is non-empty.

def max_value(nums):
    maxValue = float('-inf')
    
    for x in nums:
        if x > maxValue:
            maxValue = x

    return maxValue




print(max_value([4, 7, 2, 8, 10, 9])) # -> 10
print(max_value([10, 5, 40, 40.3])) # -> 40.3
print(max_value([-5, -2, -1, -11])) # -> -1
print(max_value([42])) # -> 42
print(max_value([1000, 8])) # -> 1000
print(max_value([1000, 8, 9000])) # -> 9000
print(max_value([2, 5, 1, 1, 4])) # -> 5