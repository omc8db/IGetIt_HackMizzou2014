##
##
##This file is DEPRECIATED. It is kept around for reference, and is
##candidate for DELETION
##

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
    def connect(self, dbname):
        try:
            self.con = lite.connect(dbname)    
            self.cur = self.con.cursor()
            
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)        
    def update(aggregate):
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
