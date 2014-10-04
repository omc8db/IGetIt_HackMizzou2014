import sqlite3
import threading

class LockableCursor:
    def __init__ (self, cursor):
        self.cursor = cursor
        self.lock = threading.Lock ()

    def execute (self, arg0, arg1 = None):
        self.lock.acquire ()

        try:
            self.cursor.execute (arg1 if arg1 else arg0)

            if arg1:
                if arg0 == 'all':
                    result = self.cursor.fetchall ()
                elif arg0 == 'one':
                    result = self.cursor.fetchone ()
        except Exception as exception:
            raise exception

        finally:
            self.lock.release ()
            if arg1:
                return result

def dictFactory (cursor, row):
    aDict = {}
    for iField, field in enumerate (cursor.description):
        aDict [field [0]] = row [iField]
    return aDict

class Db:
    def __init__ (self, app):
        self.app = app

    def connect (self):
        self.connection = sqlite3.connect (self.app.dbFileName, check_same_thread = False, isolation_level = None)  # Will create db if nonexistent
        self.connection.row_factory = dictFactory
        self.cs = LockableCursor (self.connection.cursor ())
