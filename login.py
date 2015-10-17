import sqlite3
import md5

#checks if username + password matches one in database
#if not, add username + password to database
def checkuser(username,password):
    m= md5.new()
    m.update(password)
    password = m.hexdigest()
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
                conn.close()
                return "in"
            else:
                #print "incorrect password"
                conn.close()
                return "<h3> Wrong Password </h3>"
    else:
        conn.close()
        return "<h3> No Such User <h3>"    

def adduser(uname,passwd):
    m= md5.new()
    m.update(passwd)
    passwd = m.hexdigest()
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    TEMPLATE="INSERT INTO users VALUES('%(username)s','%(password)s')"
    q = TEMPLATE%{'username' : uname, 'password' : passwd}
    c.execute(q)
    conn.commit()
    conn.close()
    

#adduser("a","123")
#checkuser("b","1234") #expecting "added"
#checkuser("a","123") #expecting "correct password"
#checkuser("b","123") #expecting "incorrect password"
    
