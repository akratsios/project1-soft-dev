import random
from pymongo import MongoClient

def addblog(t, un, post):    
    #inserts new blog into the blogs table
    connection = sqlite3.connect("database.db")
    c = connection.cursor()

    ID = getcount("blogs") + 1
    
    #just in case it's the first blog ever
    c.execute("CREATE TABLE IF NOT EXISTS blogs (title TEXT, BID INTEGER, username TEXT, post TEXT)")

    TEMPLATE = "INSERT INTO blogs VALUES (\"%(title)s\", %(BID)s, \"%(username)s\", \"%(post)s\");"
    q = TEMPLATE%({"title":t, "BID":ID, "username":un, "post":post})
    c.execute(q)

    connection.commit()
    connection.close()

def addcomment(BID, un, cmt):
    #inserts new comment into the comments table
    connection = sqlite3.connect("database.db")
    c = connection.cursor()
    
    CID = getcount("comments") + 1
    
    #just in case it's the first comment ever
    c.execute("CREATE TABLE IF NOT EXISTS comments (CID INTEGER, BID INTEGER, username TEXT, comment TEXT)")
    
    TEMPLATE = "INSERT INTO comments VALUES(%(CID)s, %(BID)s, \"%(username)s\", \"%(comment)s\");" 
    q = TEMPLATE%({"CID":CID, "BID":BID, "username":un, "comment":cmt})
    c.execute(q)

    connection.commit()
    connection.close()

def getblogs(start, end):
    #returns list of blogs with IDs from start to end
    connection = sqlite3.connect("database.db")
    c = connection.cursor()
    
    TEMPLATE = "SELECT * FROM blogs WHERE BID >= %(st)s AND BID <= %(end)s"
    q = TEMPLATE%({"st":start, "end":end})
    result = c.execute(q)
    bloglist = []
    for row in result:
        bloglist.append(row)
    return bloglist

def getoneblog (BID):
    #displays the blog whose blog ID matches BID
    connection = sqlite3.connect("database.db")
    c = connection.cursor()

    TEMPLATE = "SELECT * FROM blogs WHERE BID = %(blogid)s"
    q = TEMPLATE%({"blogid":BID})
    result=c.execute(q)
    
    bloginfo = []
    for data in result:
        bloginfo.append(data)
    return bloginfo

def getblogcomments (BID):
    #displays the comments whose CID matches BID
    connection = sqlite3.connect("database.db")
    c = connection.cursor()

    TEMPLATE = "SELECT comments.username, comments.comment FROM comments WHERE BID = %(blogid)s"
    q = TEMPLATE%({"blogid":BID})
    result=c.execute(q)
    
    commentinfo = []
    for data in result:
        commentinfo.append(data)
    return commentinfo

def getcount(source):
    connection = sqlite3.connect("database.db")
    c = connection.cursor()
    TEMPLATE = "SELECT COUNT(*) FROM %(source)s"
    q = TEMPLATE%({"source" : source})
    result = c.execute(q)
    for data in result:
        return data[0]
