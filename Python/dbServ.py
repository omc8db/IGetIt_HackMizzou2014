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
POLL_DELAY = .005
MAX_PREFIX = 1
DELIMITER = ';'

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
        self.inputfile = open(PIPE_IN_NAME, 'w')
        self.inputfile.write("")
        self.inputfile.flush()
        self.inputfile.close()

        ##Clear the output buffers
        for prefix in range(0, MAX_PREFIX):
            f = open(PIPE_OUT_PREFIX + str(prefix), 'w')
            f.write("")
            f.flush()
            f.close()
        
        ##Open for reading
        self.inputfile = open(PIPE_IN_NAME, 'r')

        ##Connect to Database
        self.dbcon = lite.connect(dbname)
        self.cur = self.dbcon.cursor()
        
    def __del__(self):
        self.inputfile.close()
        self.dbcon.close()
        
    def poll(self):
        queries = []
        queries.append(self.inputfile.read())
        if(len(queries[0]) > 0):
            print len(queries[0])
            queries = queries[0].split(';')
            print "Executing " + str(len(queries)) + " Queries"
            for query in queries[:-1]: ##All but the last query. The last query is empty
            #remove prefix from query
                prefix = query[0]
                query = query[1:]
                query = query + ";"
                print "Executing " + query
                result = self.exec_input(query)
                
                g = open(PIPE_OUT_PREFIX + str(prefix), "a")
##                g.write(str(result))
##                g.write(DELIMITER)
                packer = pickle.Pickler(g)
                packer.dump(result)
                g.close()
    def infpoll(self):
        while(1):
            self.poll();
            time.sleep(POLL_DELAY)
        
    def exec_input(self, query):
        try:
            self.cur.execute(query)
        except:
            print "ERROR. Could not execute query."
        result = self.cur.fetchall()
        return result
        
        #pass input to SQLite
        
     
