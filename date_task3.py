from datetime import date, timedelta


def next_monday(text):
    d = date.fromisoformat(text)
    days_ahead = 7 - d.weekday()
    return d + timedelta(days=days_ahead)


print(next_monday("2026-09-26"))
print(next_monday("2026-09-27"))
print(next_monday("2026-09-28"))