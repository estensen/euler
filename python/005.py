# Smallest positive number divisible by nums 1-20
from fractions import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

print(reduce(lcm, range(1, 20+1)))
