from datetime import date


Days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]

def day_of_week(d):
    date_full = date.fromisoformat(d)
    day = date_full.weekday()
    return Days[day]

print(day_of_week("2026-09-30"))
print(day_of_week("2026-09-28"))
print(day_of_week("2000-01-01"))
