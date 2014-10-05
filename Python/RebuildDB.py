##
##RebuildDB
##Rebuilds Database
##
##
DB_FILENAME = "data.db"

import sqlite3 as lite
import sys

con = lite.connect(DB_FILENAME)

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE Interest;")
    cur.execute("DROP TABLE devices;")
    cur.execute("CREATE TABLE Interest(Id INTEGER PRIMARY KEY, rating REAL, time INT, student INT);")
    cur.execute("CREATE TABLE devices(mac TEXT PRIMARY KEY, ip TEXT, student INT);")
