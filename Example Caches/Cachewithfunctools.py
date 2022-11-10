"""
Example program that uses the functools library's cache decorator to cache functions

Pros:
-No clutter added to global namespace
-Compact
-Readable
-Cache is automatically implemented via function decorator
-No work has to be done by the caller for the cache to work
Cons:
-No control over what is cached (return is always cached)
-External dependency (functools)
"""

from functools import cache


@cache
def factorialwithfunctoolscache(n: int):
    if n:
        return n * factorialwithfunctoolscache(n - 1)
    else:
        return 1
