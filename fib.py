"""
Simple Fibonacci algorithm
"""


def fib(n):
    if n < 2:
        return 1
    else:
        fib(n-1) + fib(n-2)
