from datetime import datetime


def is_valid_date(text):
    """Check whether text is a valid date in the format YYYY-MM-DD.

    Returns True if it is a real date in exactly this format,
    otherwise returns False.
    """
    if len(text) != 10:
        return False
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


print(is_valid_date("2026-10-03"))
print(is_valid_date("2024-02-29"))
print(is_valid_date("2026-02-30"))
print(is_valid_date("2026-13-01"))
print(is_valid_date("03.10.2026"))
print(is_valid_date("2026-1-5"))