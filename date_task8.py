from datetime import datetime


def seconds_between(time1, time2):
    """Return how many seconds passed between two moments.

    Both moments must be text in the format "YYYY-MM-DD HH:MM:SS".
    The order of the two moments does not matter.
    If a format is wrong, prints a message and returns None.
    """
    try:
        t1 = datetime.fromisoformat(time1)
        t2 = datetime.fromisoformat(time2)
    except ValueError:
        print("Неправильний формат. Використовуйте YYYY-MM-DD HH:MM:SS")
        return None
    difference = t2 - t1
    return int(abs(difference.total_seconds()))


print(seconds_between("2026-10-03 13:00:00", "2026-10-03 13:01:30"))
print(seconds_between("2026-10-03 12:00:00", "2026-10-03 14:00:00"))
print(seconds_between("2026-10-03 23:59:50", "2026-10-04 00:00:10"))
print(seconds_between("03.10.2026 13:00", "2026-10-03 13:01:30"))