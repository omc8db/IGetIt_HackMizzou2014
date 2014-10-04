##
##DB Serv
##Parses SQL queries and places the output in named pipes
##
##

import pickle
import sqlite3 as lite
PIPE_IN_NAME = '\\.\pipe\DB_Query_in'
PIPE_OUT_PREFIX = '\\.\pipe\DB_Query_out'
DB_NAME = "data.db"

pickle.HIGHEST_PROTOCOL = 2             #Binary data serialization

def initPipes():

class db_Serv:
    con = None
    f = None
    db_name = None
    def __init__(self, dbname):
        f.open(PIPE_IN_NAME, r)
        db_name = dbname
    def poll():
        try:                 #Query found
            query = f.read()
            #remove prefix from query
            prefix = query[0]
            result = exec_input(query[1:])
            g.open(PIPE_OUT_PREFIX + str(prefix), r)
            packer = pickle.Pickler(g, HIGHEST_PROTOCOL)
            packer.dump(result)
            g.close
        except:              #No query found
            ()

        
    def exec_input(query):
        self.con = lite.connect(dbname)
        self.cur = self.con.cursor()
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result
        
        #pass input to SQLite
        
     
