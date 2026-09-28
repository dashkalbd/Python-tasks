import math


def cos_degrees(angle):
    radians = math.radians(angle)
    return round(math.cos(radians), 4)


print(cos_degrees(0))
print(cos_degrees(60))
print(cos_degrees(90))
print(cos_degrees(180))