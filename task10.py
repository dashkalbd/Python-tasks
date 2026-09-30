import math


def to_polar(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return round(r, 4), round(theta, 4)


print(to_polar(3, 4))
print(to_polar(1, 1))
print(to_polar(0, 2))
print(to_polar(-1, 0))