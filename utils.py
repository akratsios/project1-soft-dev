import sqlite3

connection = sqlite3.connect("database.db")
c = connection.cursor()

def addblog(t, ID, un, post):    
    #inserts new blog into the blogs table
    connection = sqlite3.connect("database.db")
    c = connection.cursor()
    #just in case it's the first blog ever
    c.execute("CREATE TABLE IF NOT EXISTS blogs (title TEXT, BID INTEGER, username TEXT, post TEXT)")

    TEMPLATE = "INSERT INTO blogs VALUES (\"%(title)s\", %(BID)s, \"%(username)s\", \"%(post)s\");"
    q = TEMPLATE%({"title":t, "BID":ID, "username":un, "post":post})
    c.execute(q)

def addcomment(CID, BID, un, cmt):
    #inserts new comment into the comments table
    connection = sqlite3.connect("database.db")
    c = connection.cursor()
    #just in case it's the first comment ever
    c.execute("CREATE TABLE IF NOT EXISTS comments (CID INTEGER, BID INTEGER, username TEXT, comment TEXT)")
    
    TEMPLATE = "INSERT INTO comments VALUES(%(CID)s, %(BID)s, \"%(username)s\", \"%(comment)s\");" 
    q = TEMPLATE%({"CID":CID, "BID":BID, "username":un, "comment":cmt})
    c.execute(q)



addcomment(1, 69, "RarestPepe", "hey everyone it's a me Mario")



