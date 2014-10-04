#!/usr/bin/python
# -*- coding: utf-8 -*-

######################################################
#   Database management and updating thread
#   
#
######################################################

from some_class import *
from database import *

db = database(DB_NAME)
students = setup_students()

aggregate = [0,0,0,0] #[[[rating, time] [rating, time]][rating, time]
samples = 0
DB_UPDATE_PERIOD = 200 #number of cycles of data to collect before
                       #storing in the database
POLL_FREQ = 5

setup_students()

f = url.urlopen('http://192.168.137.112')
while(1):
    temp = 0
    while temp < DB_UPDATE_PERIOD:
        temp = temp + 1
        pres_time = time.time()
        for stud in range in students:
            present[stud] = students[stud].getrating()
            aggregate[stud].append([students[stud].rating, pres_time, students[stud].ID])
        time.sleep(POLL_FREQ)
    db.update(aggregate)
    aggregate = [0,0,0,0]

