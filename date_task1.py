from datetime import date


def days_between(date1, date2):
    d1 = date.fromisoformat(date1)
    d2 = date.fromisoformat(date2)
    difference = d2 - d1
    return abs(difference.days)


print(days_between("2026-01-01", "2026-09-26"))
print(days_between("2026-12-25", "2026-12-01"))