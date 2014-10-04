##
##DevicePoll
##Polls devices
##
##

import sys
import time
import urllib2 as url
import dbClient
PIPE_ID = 0
POLL_DELAY = 5   #Seconds to delay while polling

class devicePoll:
    conn = None
    devices = []
    inpipe = None
    primekey = 0
    def __init__(self):
        self.conn = dbClient.db_Connect(PIPE_ID)
        #get unique primary key
        all_events = conn.get_all_events()
        primekey = all_events[len(all_events)][0]   #fetches the last event
    def infpoll(self):
        while (1):
            self.poll()
            x = self.conn.read()
            if x:
                devices.append(x)
    def poll(self):
        curr_time = time.time()
        for device in devices:
            val = talk(device)
            self.conn.sendEvents([primekey, val, curr_time, device.owner])
            primekey++
    def talk(device):
        #make http request to device
        f = url.urlopen(device.ip)
        rating = f.read()
        return rating

class device:
    ip = None
    mac = None
    owner = None
    def __init__(self, ip, mac, owner)
        self.ip = ip
        self.mac = mac
        self.owner = owner
    def __init__(self, db_entry)
        self.mac = db_entry[0]
        self.ip = db_entry[1]
        self.owner = db_entry[2]
        
            
    
