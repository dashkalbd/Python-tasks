import math


def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c              # discriminant
    if d > 0:                           # two roots
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return [x1, x2]
    elif d == 0:                        # one root
        return [-b / (2 * a)]
    else:                               # no real roots
        return []


print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1, 2, 1))
print(solve_quadratic(1, 0, 1))