import math


def arc_length(radius, angle):
    """angle must be in radians"""
    return radius * angle


print(arc_length(10, math.pi / 2))
print(arc_length(5, math.pi))