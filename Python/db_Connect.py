##
##DB Connect
##Generates SQL queries and places them in a FIFO pipe to be handled by the
##database server software
##


import pickle
import sys

PIPE_IN_NAME = 'servin.txt'
PIPE_OUT_PREFIX = 'servout'
pickle.HIGHEST_PROTOCOL = 2             #Binary data serialization    


##USAGE
##Define a PIPE_ID for your thread
##pass this as the argument to your db_Connect object
##This will create a pipe with an ID associated with your thread

class db_Connect:
    f = None              #File
    iden = None           #Integer Identifier
    def __init__(self, iden):
        #define the named pipe
        self.iden = iden

    #Prefixes the command with an identifier for the output pipe
    def send(self, command):
        #open pipe
        try:
            f = open(PIPE_IN_NAME, 'w')
            f.write(str(iden) + str(command))
            f.flush()
            f.close()
        except:
            ()
         
        
    def read(self):
        g = open(PIPE_OUT_PREFIX + str(self.iden), 'r')
        #unpickle
        dePickler = pickle.Unpickler(g);
        try:
            output = dePickler.load();
        except:
            output = None

    #gets events with a specific time stamp
    def get_time_ratings(self, time):
        query = "SELECT rating FROM Interest WHERE time = " + time + ";"
        self.send(query)
        result = self.read()
        return result

    #get maximum time
    def get_max_time(self):
        query = "SELECT MAX(time) FROM Interest;"
        self.send(query)
        result = self.read()
        return result

##   Not user about the best query to use here 
##    def get_recent_events():
##        query = "SELECT * FROM Interest WHERE time "
##        send(query)
##        result = read()
##        return result
    def get_all_events(self):
        query = "SELECT * FROM Interest;"
        self.send(query)
        result = self.read()
        return result
    def lookup_student(self, mac_addr):
        query = "SELECT * FROM devices where mac = " + str(mac_addr) + ";"
        self.send(query)
        result = self.read()
        return result[0]
    
    #Pass variables as sendEvents([index, rating, time, student])
    def sendEvents(self, entry):                   
        query = "INSERT INTO Interest VALUES ("
        query = query + enterid + ',' + entry[0] + ',' + entry[1] + ',' + entry[2] + ")"
        self.send(query)
    def addDevice(self, mac, ip, student):
        #addDevice should also result in an echo being sent to output pipe 0
        query = "INSERT INTO devices VALUES (" + mac + "," + ip + "," + student + ");"
        
        #query to add device
        #query to select * from devices where mac = mac
        
