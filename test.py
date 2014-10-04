import urllib2 as url
import time

setup_students()

student[]
present[]
aggregate[]
samples = 0
db_update_period = 200 #big numbers, fire good
poll_freq = 5

setup_students()

f = url.urlopen('http://192.168.137.112')
while(1):
    temp = 0
    while temp < db_update_period:
        temp = temp + 1
        for student in students:
            present[student] = student.getrating()
        #update aggregate
        time.sleep(5)
    db.update()
