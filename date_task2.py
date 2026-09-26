from datetime import date


def format_date(text):
    d = date.fromisoformat(text)
    return d.strftime("%d/%m/%Y")


print(format_date("2026-09-26"))   # 26/09/2026
print(format_date("2025-01-05"))   # 05/01/2025