import MySQLdb

class DBConnection(object):
    
    db = MySQLdb.connect(
                    host="172.17.0.1",
                    user="root",
                    passwd="Redhat@123",
                    db="project"
                  )
    dictCursor =  db.cursor(MySQLdb.cursors.DictCursor)