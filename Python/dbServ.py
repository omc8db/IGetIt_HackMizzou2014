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
    con = None
    f = None
    db_name = None
    def __init__(self, dbname):
        f = open(PIPE_IN_NAME, 'r')
        db_name = dbname
    def poll(self):
        try:                 #Query found
            query = f.read()
            #remove prefix from query
            prefix = query[0]
            result = exec_input(query[1:])
            g.open(PIPE_OUT_PREFIX + str(prefix), w)
            packer = pickle.Pickler(g, HIGHEST_PROTOCOL)
            packer.dump(result)
            g.close
        except:              #No query found
            ()
    def infpoll(self):
        while(1):
            self.poll();
            time.sleep(POLL_DELAY)
        
    def exec_input(self, query):
        self.con = lite.connect(dbname)
        self.cur = self.con.cursor()
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result
        
        #pass input to SQLite
        
     
