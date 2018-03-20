from datetime import datetime

time = datetime.now()
print time

year = time.year
month = time.month
day = time.day
hour = time.hour
minute = time.minute
seccond = time.second
print time.strftime("%Y-%m-%d %H:%M:%S")
