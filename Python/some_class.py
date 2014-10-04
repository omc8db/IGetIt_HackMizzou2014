
import sqlite3 as lite
import sys
import urllib2 as url
import time
#import numpy

IP_CONST = '192.168.137.112'
MAC_CONST = '4344A6084119'
DB_NAME = "database.db"
class database:
    enterid = 0
    con = None
    cur = None
    def __init__(self, dbname):
        self.con = self.connect(dbname)
        #update enterid
    def __del__(self):
        if con:
            con.close()
    def connect(dbname):
        try:
            con = lite.connect(dbname)    
            cur = con.cursor()
            
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)        
    def update(aggregate[]):
        cur = con.cursor()
        for stud in aggregate:
            for entry in stud:
                query = "INSERT INTO Interest VALUES ("
                query = query + enterid + ',' + entry[0] + ',' + entry[1] + ',' + entry[2] + ")"
                cur = con.cursor()
                cur.execute(query)
        
    def get_student_id(device):
        #Set up query
        query = "SELECT student FROM mac_addresses where mac_addr = "
        query = query + device.mac_addr

        #Execute Query
        cur.execute(query)
        data = cur.fetchone()

        return data[0]        

class student:
    ID
    dev       #device
    rating
    def getrating():
        f = url.urlopen(thing.ip_addr)
        rating = f.read()
        return rating

class device:
    ip_addr
    mac_addr
    def __init__(self, ip, mac):
        ip_addr = ip
        mac_addr = mac
    

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
    a_list[]
    a_list.append(IP_CONST)
    return a_list

def dev_connect(): #receive data from device
    #unpackage data
    #extract ip and  mac
    device thingy
    thingy.ip_addr = IP_CONST
    thingy.mac_addr = MAC_CONST
    return thingy
