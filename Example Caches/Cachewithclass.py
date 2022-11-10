"""
Example program that uses a list to cache functions

Pros:
-Cache can be manually reset by creating a new instance
-No clutter added to global namespace
-Compact
-No work has to be done by the caller for the cache to work
-No external dependencies (typing doesn't count as it is not required for the code to work)
-Ability to control what is cached, rather than just caching return
-Cache can be easily reset, read, and modified via class field
Cons:
-Makes function harder to read and more cluttered
-Cache must be manually implemented
-Class instance must be created
-Creating a new instance will always reset cache, which may be undesirable
-Less compact than a single function
"""

from typing import Any


class Factorial:
    def __init__(self):
        self.cache: dict[Any, Any] = {}

    def factorialwithclasscache(self, n: int):
        if n:
            if n in self.cache:
                result = self.cache[n]
            else:
                result = n * self.factorialwithclasscache(n - 1)
                self.cache[n] = result
            return result
        else:
            return 1
