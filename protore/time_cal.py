#time_cal.py
#s24015


import calendar as cal
import datetime
print(cal.month(2024,6))
now = datetime.datetime.now()
print(now.strftime("%Y年%M月%D日 %H:%M:%S"))
