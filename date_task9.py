from datetime import date, timedelta


def date_after_days(days):
    """Return the date that is the given number of days after today.

    days must be a whole number, e.g. 10 or "10".
    Negative numbers go back in time.
    If days is not a whole number, prints a message and returns None.
    """
    try:
        days = int(days)
    except ValueError:
        print("Кількість днів має бути цілим числом")
        return None
    return date.today() + timedelta(days=days)


print(date_after_days(10))
print(date_after_days(30))
print(date_after_days(-3))
print(date_after_days("abc"))