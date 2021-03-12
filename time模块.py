import datetime
import time

print(time.time())
print(time.clock())
t = time.localtime()
print(time.ctime())
print(t)
print(t.tm_mday)
print(time.mktime(t))
# print(time.strftime('time.time()','%Y-%m-%D'))
print(time.strftime('%Y-%m-%d'))
print('jjjjjjjjjjjj')
print(time.strftime('%Y-%m-%d %H:%M:%S'))
t1 = time.strptime('2019/09/28','%Y/%m/%d')
print(t1)
print(t1.tm_year,"-",t1.tm_mon,"-",t1.tm_yday)

timedelta = datetime.timedelta(weeks=3)
now = datetime.datetime.now()
result = now + timedelta
print(result)