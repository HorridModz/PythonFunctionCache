"""
Example program that uses a default argument to cache functions

Pros:
-No clutter added to global namespace
-Compact
-No work has to be done by the caller for the cache to work
-No external dependencies (typing doesn't count as it is not required for the code to work)
-Ability to control what is cached, rather than just caching the return
Cons:
-Makes function harder to read and more cluttered
-Cache must be manually implemented
-Cache cannot be easily reset without work from the caller (can be done with functools.partial,
by saving an instance of the old function and setting the function back to that old instance,
or by adding an argument to the function that resets the cache)
-Mutable default argument is considered bad practice
"""

from typing import Any


def factorialwithdefaultargumentcache(n: int, cache: dict[Any, Any] = {}):
    if n:
        if n in cache:
            result = cache[n]
        else:
            result = n * factorialwithdefaultargumentcache(n - 1)
            cache[n] = result
        return result
    else:
        return 1

