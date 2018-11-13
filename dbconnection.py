import sqlite3
import sys


class DBConnection(object):

    dbPath = sys.path[0]+"/database.db"
    db = sqlite3.connect(
        dbPath
    )
    db.row_factory = sqlite3.Row
    dictCursor = db.cursor()
