##
##DB Serv
##Parses SQL queries and places the output in named pipes
##
##


import pickle
import sqlite3 as lite
import os
import time
PIPE_IN_NAME = 'servin.txt'
PIPE_OUT_PREFIX = 'servout'
DB_NAME = "data.db"
POLL_DELAY = 2

pickle.HIGHEST_PROTOCOL = 2             #Binary data serialization

##Open pipes
def initPipes():
    ()
    #os.popen

class db_Serv:
    dbcon = None     #database connection
    cur = None       #database cursor
    inputfile = None #command source
    def __init__(self, dbname):

        ##Clear the input
        inputfile = open(PIPE_IN_NAME, 'w')
        inputfile.write("")
        inputfile.flush()
        inputfile.close()

        ##Open for reading
        inputfile = open(PIPE_IN_NAME, 'r')

        ##Connect to Database
        self.dbcon = lite.connect(db_name)
        self.cur = self.con.cursor()
        
    def __del__(self):
        inputfile.close()
        dbcon.close()
        
    def poll(self):
        try:                 #Query found
            queries = []
            queries.append(inputfile.read())
            queries[0].split(';')
            for query in queries:
            #remove prefix from query
                prefix = query[0]
                result = exec_input(query[1:])
                g.open(PIPE_OUT_PREFIX + str(prefix), "a")
                packer = pickle.Pickler(g, HIGHEST_PROTOCOL)
                packer.dump(result)
                g.close()
        except:              #No query found
            print "WARNING: COULD NOT RETURN QUERY RESULTS"
    def infpoll(self):
        while(1):
            self.poll();
            time.sleep(POLL_DELAY)
        
    def exec_input(self, query):
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result
        
        #pass input to SQLite
        
     
