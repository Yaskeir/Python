# Mateusz Fido

import timeit
from functools import lru_cache

def exec_time(func, *args):
    '''Return an evaluation of time (in seconds) required to run a given function'''
    start = timeit.default_timer()
    func(*args)
    end = timeit.default_timer()
    return end - start

def fibonacci_rec(n):
    '''Return the nth term of the fibonacci sequence, a recursive implementation written in class'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2) 

def fibonacci_iter(n):
    '''Return the nth term of the fibonacci sequence, a linear iterative implementation written in class'''
    if n == 0:
        second = 0
    else: 
        first = -1
        second = 0
        placeholder = 1
        for i in range(n):
            first = placeholder
            placeholder = second
            second = first + placeholder
    return second


# Functions found at https://dev.to/teosoft7/how-to-implement-fibonacci-sequence-with-python-4cfo
# Making use of caching the previous results

cache = {}

def fibonacci_cache(num):
    '''Return a fibonacci sequence value of num'''

    if num in cache:
        return cache[num]

    if num == 0:
        result = 0
    elif num == 1 or num == 2:
        result = 1
    else:
        result = fibonacci_cache(num - 2) + fibonacci_cache(num - 1)

    cache[num] = result
    return result

@lru_cache(maxsize = 1000)

def fibonacci_lru(num):
    '''Return a fibonacci sequence value of num'''

    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1

    return fibonacci_lru(num - 2) + fibonacci_lru(num - 1)



#print("My recursive version took", exec_time(fibonacci_rec, 10), "seconds to run.")
#print("My iterative version took", exec_time(fibonacci_iter, 10), "seconds to run.")
#print("The version using an explicit cache took", exec_time(fibonacci_cache, 10), "seconds to run.")
#print("The version using an implicit cache imported from a library took", exec_time(fibonacci_lru, 10), "seconds to run.")
