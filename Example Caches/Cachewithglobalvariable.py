"""
Example program that uses a default argument to cache functions

Pros:
-Compact
-No work has to be done by the caller for the cache to work
-No external dependencies (typing doesn't count as it is not required for the code to work)
-Ability to control what is cached, rather than just caching the return
-Cache can be easily reset, read, and modified via global variable
Cons:
-Uses a global variable
-Makes function harder to read and more cluttered
-Cache must be manually implemented
"""

from typing import Any

cache: dict[Any, Any] = {}


def factorialwithglobalvariablecache(n: int):
    if n:
        if n in cache:
            result = cache[n]
        else:
            result = n * factorialwithglobalvariablecache(n - 1)
            cache[n] = result
        return result
    else:
        return 1
