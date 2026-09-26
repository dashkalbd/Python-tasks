import math


def log_iterations(x):
    count = 0
    while x >= 1:
        x = math.log(x)
        count = count + 1
    return count


print(log_iterations(100))
print(log_iterations(10))
print(log_iterations(0.5))