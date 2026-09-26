from datetime import datetime
import time


def duration(start, end):
    difference = end - start
    return difference.total_seconds()


start = datetime.now()
time.sleep(2)
end = datetime.now()

print("Тривалість:", duration(start, end), "секунд")