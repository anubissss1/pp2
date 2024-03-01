# Ex1
import datetime
before = datetime.datetime.now().date()
after = datetime.timedelta(days=5)

new = before - after

print("Current date:", before)
print("Five days ago:", new)

# ex2
import datetime
before = datetime.datetime.now().date()
delta = datetime.timedelta(days=1)

yesterday = before - delta
tomorrow = before + delta

print("Yesterday :", yesterday)
print("Today :", before)
print("Tomorrow :", tomorrow)

# ex3
import datetime
time = datetime.datetime.now()
after_time = time.replace(microsecond = 0)
print("Time without microsecond:",after_time)

# ex4
import datetime 
date1 = datetime.datetime(2024,2,17,12,1,0)
date2 = datetime.datetime(2024,2,17,12,1,23)
difference = date2 - date1
print(difference)