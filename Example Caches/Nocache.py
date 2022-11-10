"""
Example program that does not use a cache
"""


def factorialwithoutcache(n: int):
    if n:
        return n * factorialwithoutcache(n - 1)
    else:
        return 1
