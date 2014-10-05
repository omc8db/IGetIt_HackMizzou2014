##
##DB Connect
##Generates SQL queries and places them in a FIFO pipe to be handled by the
##database server software
##


import pickle
import sys
import time

PIPE_IN_NAME = 'servin.txt'
PIPE_OUT_PREFIX = 'servout'
PICKLE_TIME_DELAY = 0.01      #time to wait for database output to catch up
DELIMITER = ';'

##USAGE
##Define a PIPE_ID for your thread
##pass this as the argument to your db_Connect object
##This will create a pipe with an ID associated with your thread

class db_Connect:
    f = None              #File for output
    iden = None           #Integer Identifier
    inputfile = None              #File for input
    def __init__(self, iden):
        #define the named pipe
        self.iden = iden

        #clear the 
        self.inputfile = open(PIPE_OUT_PREFIX + str(self.iden), 'r')

    def __del__(self):
        self.inputfile.close()

    #Prefixes the command with an identifier for the output pipe
    def send(self, command):
        #open pipe
        success = 0
        while(success==0):
##        try:
            outputfile = open(PIPE_IN_NAME, 'a')
            outputfile.write(str(self.iden) + str(command))
            outputfile.flush()
            outputfile.close()
            success = 1
##        except:
##            outputfile.close()
         
        
    def read(self):

##  WORST SERIALIZATION PROTOCOL IN THE WORLD
##        db_out = ""
##        done = 0
##        while(done == 0):
##            print "Not done yet"
##            try:
##                n = inputfile.read(1)
##                print n
##                if(n==DELIMITER):
##                    print "Delimeter Found"
##                    done = 1
##                else:
##                    db_out = db_out + n
##            except:
##                time.sleep(PICKLE_TIME_DELAY)
##        ##output = eval(db_out)
##        output = db_out
##        return output
            
        
        
        #unpickle
        time.sleep(PICKLE_TIME_DELAY)
        dePickler = pickle.Unpickler(self.inputfile);
        success = 0
        while(success = 0):
            try:
                output = dePickler.load();
                success = 1
            except:
                time.sleep(PICKLE_TIME_DELAY)
        return output

    #gets events with a specific time stamp
    def get_time_events(self, time):
        query = "SELECT * FROM Interest WHERE time = " + time + ";"
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
        query = query + self.enterid + ',' + entry[0] + ',' + entry[1] + ',' + entry[2] + ")"
        self.send(query)
    def addDevice(self, mac, ip, student):
        #addDevice should also result in an echo being sent to output pipe 0
        query = "INSERT INTO devices VALUES (\"" + mac + "\",\"" + ip + "\"," + student + ");"
        self.send(query)
        query = "SELECT * FROM devices WHERE mac = \"" + mac + "\";"
        self.send(query)
        result = self.read()  ##Ignore this, we send 2 queries
        result = self.read()
        return result
        
        #query to add device
        #query to select * from devices where mac = mac
        
