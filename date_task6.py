from datetime import date


def days_until_birthday(birthday, today):
    b = date.fromisoformat(birthday)
    t = date.fromisoformat(today)
    next_birthday = date(t.year, b.month, b.day)
    if next_birthday < t:
        next_birthday = date(t.year + 1, b.month, b.day)
    return (next_birthday - t).days


print(days_until_birthday("2000-12-25", "2026-09-30"))
print(days_until_birthday("1999-09-30", "2026-09-30"))
print(days_until_birthday("2001-05-10", "2026-09-30"))

# with the real current date:
print(days_until_birthday("2000-12-25", date.today().isoformat()))