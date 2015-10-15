import sqlite3

conn = sqlite3.connect("names.db")
c = conn.cursor()

def fetch(item):
    if item == "user":
        q = "SELECT names.user FROM names"
    elif item == "passwd":
        q = "SELECT names.passwd FROM names"
    result = c.execute(q)
    return result

def checkuser(username,password):
    if username in fetch("user"):
        if password == fetch("passwd")[user]:
            return true
        else:
            return false
    else:
        adduser(username,password)

def adduser(uname,passwd):
    TEMPLATE="INSERT INTO names VALUES('%(username)s',%(password)s)"
    q = TEMPLATE%uname
    r = TEMPLATE%passwd
    c.execute(q)
    c.execute(r)

conn.commit()
    
