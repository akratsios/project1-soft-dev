import random
from pymongo import MongoClient

import md5

#checks if username + password matches one in database
#if not, add username + password to database
def create():
    connection = MongoClient()
    db=connection["database.db"]

    db.users.insert_one(
        {
            "username": "",
            "password": ""
        }
    )

    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

def checkuser(username,password):
    create()
    m= md5.new()
    m.update(password)
    password = m.hexdigest()
    #conn = sqlite3.connect("database.db")
    conn = connect("localhost:8000/database") #mongodb
    #c = conn.cursor()
    #^^db.inventory.find({type: 'a'});
    #a = """
    #SELECT users.username,users.password 
    #FROM users
    #WHERE users.username = '%s'""" %username
    a = """
    db.users.find(
    { },
    { username: 1, password: 1, status: "%s"}
    )
    """ #more mongodb stuff
    #result = c.execute(a)
    for r in result:
        print r
        if r[0] == username:
            if r[1] == password:
                #print "correct password"
                conn.close()
                return "in"
            else:
                #print "incorrect password"
                conn.close()
                return "Wrong Password"
    else:
        conn.close()
        return "No Such User"    

def adduser(uname,passwd):
    create()
    m= md5.new()
    m.update(passwd)
    passwd = m.hexdigest()
    #conn = sqlite3.connect("database.db")
    conn = connect("localhost:8000/database") #mongodb
    #c = conn.cursor()
    db.inventory.find({}) #mongodb
    TEMPLATE="INSERT INTO users VALUES('%(username)s','%(password)s')"
    q = TEMPLATE%{'username' : uname, 'password' : passwd}
    c.execute(q)
    conn.commit()
    conn.close()

