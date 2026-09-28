import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


print(lcm(4, 6))
print(lcm(12, 18))
print(lcm(5, 7))