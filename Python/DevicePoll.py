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
POLL_DELAY = 3   #Seconds to delay while polling
DEV_LIST_REFRESH_INTERVAL = 10

class devicePoll:
    conn = None
    devices = []
    inpipe = None
    primekey = 0
    def __init__(self):
        self.conn = dbClient.db_Connect(PIPE_ID)
        #get unique primary key
        all_events = self.conn.get_all_events()
        if(all_events):
            self.primekey = all_events[len(all_events)][0]   #fetches the last event
        self.get_device_db()
    def infpoll(self):
        while (1):
            for i in range(0,DEV_LIST_REFRESH_INTERVAL):
                self.poll()
                time.sleep(POLL_DELAY)
            self.get_device_db()
    def poll(self):
        curr_time = time.time()
        for device in self.devices:
            val = talk(device)
            self.conn.sendEvents([primekey, val, curr_time, device.owner])
            self.primekey = self.primekey + 1
    def talk(device):
        #make http request to device
        f = url.urlopen(device.ip)
        rating = f.read()
        print "Device " + str(device.mac) + " read w/ value " + rating
        return rating

    ##Updates current device list from DB
    def get_device_db(self):
        self.devices = []
        device_db = self.conn.get_all_devices()
        for entry in device_db:
            self.devices.append(device(entry))
        return self.devices

class device:
    ip = None
    mac = None
    owner = None
    def __init__(self, ip, mac, owner):
        self.ip = ip
        self.mac = mac
        self.owner = owner
    def __init__(self, db_entry):
        self.mac = db_entry[0]
        self.ip = db_entry[1]
        self.owner = db_entry[2]
        
            
    
