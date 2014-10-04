##
##
##This file is DEPRECIATED. It is kept around for reference, and is
##candidate for DELETION
##

import sqlite3 as lite
import sys
import urllib2 as url
import time


IP_CONST = '192.168.137.112'
MAC_CONST = '4344A6084119'
DB_NAME = "database.db"


class student:
    ID = None
    dev = None      #device
    rating = None
    def getrating():
        f = url.urlopen(thing.ip_addr)
        rating = f.read()
        return rating

class device:
    ip_addr = None
    mac_addr = None
    def __init__(self, ip, mac):
        self.ip_addr = ip
        self.mac_addr = mac
    

def setup_students():
    dev_list =[] #append a bunch of devices to this shit, yo!
    student_list = []

    #connect devices
    #while(something)
        #dev_list.append device(something)
    
    #DEBUG========================================================
    test = student()
    test.ID = 1
    test.dev = device(IP_CONST, MAC_CONST)
    student_list.append(test)
    #iterate through a device list and get a list of student ids
    #create students
    return student_list
    
def get_ip_list():
    a_list = []
    a_list.append(IP_CONST)
    return a_list

def dev_connect(): #receive data from device
    #unpackage data
    #extract ip and  mac
    thingy = device(IP_CONST, MAC_CONST)
    return thingy
