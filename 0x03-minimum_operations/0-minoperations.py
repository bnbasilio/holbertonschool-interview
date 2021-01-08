#!/usr/bin/python3
"""
calculates the fewest number of Copy All and Paste operations needed
to result in exactly n H characters in a file
"""

def minOperations(n):
    if n < 2:
        return 0
    divisor, sum = 2, 0
    while divisor <= n / 2:
        if n % divisor == 0:
            n //= divisor
            sum += divisor
        else:
            divisor += 1
    return sum + n
