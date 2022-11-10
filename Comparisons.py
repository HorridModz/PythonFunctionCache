"""
Program to perform speed tests on all the cache methods
"""

from typing import Callable
import timeit
import sys
import os
from datetime import timedelta
sys.path.append(os.path.join(os.getcwd(), "Example Caches"))
from Cachewithclass import *
from Cachewithdefaultargument import *
from Cachewithfunctools import *
from Cachewithglobalvariable import *
from Nocache import *


def speedtest(name: str, function: Callable):
    totaltime = 0
    for i in range(700):
        totaltime += timeit.timeit(lambda: function(i), number=1000)
    print(f"Factorial with {name}: {timedelta(seconds=totaltime)}")


if __name__ == "__main__":
    # No cache
    speedtest("No Cache", factorialwithoutcache)
    # Cache with class
    factorial = Factorial()
    speedtest("Class Cache", factorial.factorialwithclasscache)
    # Cache with default argument
    speedtest("Default Argument Cache", factorialwithdefaultargumentcache)
    # Cache with functools
    speedtest("Functools Cache", factorialwithfunctoolscache)
    # Cache with global variable
    speedtest("Global Variable Cache", factorialwithglobalvariablecache)
