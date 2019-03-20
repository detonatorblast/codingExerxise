"""
Problem: Implement Fizz Buzz.

Constraints:
    What is fizz buzz?
        Return the string representation of numbers from 1 to n
            Multiples of 3 -> 'Fizz'
            Multiples of 5 -> 'Buzz'
            Multiples of 3 and 5 -> 'FizzBuzz'
    Can we assume the inputs are valid?
        No
    Can we assume this fits memory?
        Yes
"""

import time

def fizzbuzz(n):
    if str(n).isalpha():
        raise TypeError
    rsult = range(1, n+1)
    for i in range(len(rsult)):
        if rsult[i] % 3 == 0 and rsult[i] % 5 == 0:
            rsult[i] = 'FizzBuzz'
        elif rsult[i] % 3 == 0:
            rsult[i] = 'Fizz'
        elif rsult[i] % 5 == 0:
            rsult[i] = 'Buzz'
        else:
            rsult[i] = str(rsult[i])

    return rsult

def fizzbuzz_numpy(n):


time1 = time.time()
fizzbuzz(150000)
time2 = time.time()

print time2 - time1