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

    connection.commit()
    connection.close()

def addcomment(CID, BID, un, cmt):
    #inserts new comment into the comments table
    connection = sqlite3.connect("database.db")
    c = connection.cursor()

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
    
    TEMPLATE = "SELECT blogs.title, blogs.username, blogs.post FROM blogs WHERE BID >= %(st)s AND BID <= %(end)s"
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

    TEMPLATE = "SELECT blogs.title, blogs.username, blogs.post FROM blogs WHERE BID = %(blogid)s"
    TEMPLATE2 = "SELECT comments.username, comments.comment FROM comments WHERE CID = %(thisblogid)s"
    q = TEMPLATE%({"blogid":BID})
    q2 = TEMPLATE2%({"thisblogid":BID})
    result=c.execute(q)
    result2=c.execute(q2)
    
    bloginfo = []
    commentinfo = []
    for data in result:
        bloginfo.append(data)
    for data in result2:
        commentinfo.append(data)
    return bloginfo
    return commentinfo

def getcount():
    connection = sqlite3.connect("database.db")
    c = connection.cursor()
    result = c.execute("SELECT COUNT(*) FROM blogs")
    for data in result:
        return data

c.execute("DELETE FROM blogs")
connection.commit()
connection.close()
addblog("kek", 1, "RarestPepe", "hey everyone it's a me Mario")
addblog("whoa", 2, "Kevin", "anyone else realize it's due tomorrow???")
print getblogs(0,5)
print getcount()[0]
