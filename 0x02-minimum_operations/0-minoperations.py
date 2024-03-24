#!/usr/bin/python3
"""
Minimum operations
"""

def minOperations(n):
    """
    calculate minimum operations
    """
    if n <= 1:
        return 0
    for num in range(1, n+1):
        if n % num == 0:
            return minOperations(int(n/num)) + num

