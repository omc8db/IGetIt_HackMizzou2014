##
##DB Connect
##Generates SQL queries and places them in a FIFO pipe to be handled by the
##database server software
##

import pickle
import sys

PIPE_IN_NAME = '\\.\pipe\DB_Query_in'
PIPE_OUT_PREFIX = '\\.\pipe\DB_Query_out'
pickle.HIGHEST_PROTOCOL = 2             #Binary data serialization    

class db_Connect:
    f = None              #File
    iden = None           #Integer Identifier
    def __init__(self, iden):
        #define the named pipe
        self.iden = iden
    def send(command):
        #open pipe
        try:
            f = open(PIPE_IN_NAME, w)
            f.write(str(iden) + str(command))
            f.flush()
            f.close()
        except:
            ()
         
        
    def read():
        g.open(PIPE_OUT_PREFIX + str(iden), r)
        #unpickle
        dePickler = pickle.Unpickler(g);
        try:
            output = dePickler.load();
        except:
            output = None
    def get_time_events(time):
        query = "SELECT * FROM Interest WHERE time = " + time + ";"
        send(query)
        result = read()
        return result

##   Not user about the best query to use here 
##    def get_recent_events():
##        query = "SELECT * FROM Interest WHERE time "
##        send(query)
##        result = read()
##        return result
    def get_all_events():
        query = "SELECT * FROM Interest;"
        send(query)
        result = read()
        return result
    def lookup_student(mac_addr):
        query = "SELECT * FROM devices where mac = " + str(mac_addr) + ";"
        send(query)
        result = read()
        return result[0]
    def sendEvents(entry):                   #Pass variables as var[entry][index, rating, time, student]
        query = "INSERT INTO Interest VALUES ("
        query = query + enterid + ',' + entry[0] + ',' + entry[1] + ',' + entry[2] + ")"
        send(query)
    
        
