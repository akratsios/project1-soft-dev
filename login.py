import sqlite3

conn = sqlite3.connect("names.db")
c = conn.cursor()
#q = "create table users (username text, password text)"
#c.execute(q)
#conn.commit()
def fetch(item):
    a = ""
    if item == "user":
        a = "SELECT users.username FROM users"
    elif item == "passwd":
        a = "SELECT users.password FROM users"
    result = c.execute(a)
    for r in result:
        print r
    return result

def checkuser(username,password):
    if username in fetch("username"):
        if password == fetch("password")[user]:
            return true
        else:
            return false
    else:
        adduser(username,password)

def adduser(uname,passwd):
    TEMPLATE="INSERT INTO users VALUES('%(username)s',%(password)s)"
    q = TEMPLATE%{'username' : uname, 'password' : passwd}
    print q
    c.execute(q)
    conn.commit()

conn.commit()

adduser("a","123")
checkuser("a","123")
    
