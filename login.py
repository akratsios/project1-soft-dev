import sqlite3

#checks if username + password matches one in database
#if not, add username + password to database
def checkuser(username,password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    a = """
    SELECT users.username,users.password 
    FROM users
    WHERE users.username = '%s'""" %username
    result = c.execute(a)
    for r in result:
        print r
        if r[0] == username:
            if r[1] == password:
                #print "correct password"
                return True
            else:
                #print "incorrect password"
                return False
    else:
        conn.close()
        adduser(username,password)
        #print "added"
        return True

def adduser(uname,passwd):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    TEMPLATE="INSERT INTO users VALUES('%(username)s','%(password)s')"
    q = TEMPLATE%{'username' : uname, 'password' : passwd}
    print q
    c.execute(q)
    conn.commit()
    conn.close()

#adduser("a","123")
#checkuser("b","1234") #expecting "added"
#checkuser("a","123") #expecting "correct password"
#checkuser("b","123") #expecting "incorrect password"
    
