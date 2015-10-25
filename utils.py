import random
from pymongo import MongoClient

def addblog(t, un, post):    
    #inserts new blog into the blogs table
    connection = MongoClient()
    c = connection["blogs"]

    ID = getcount("blogs") + 1


    from datetime import datetime
    result = db.restaurants.insert_one(
        {
            "title": t,
            #"BID": ID,
            "username": un,
            "post": post
            #(still gotta figure out date stuff) "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
        }
    )
    

def addcomment(BID, un, cmt):
    #inserts new comment into the comments table
    connection = MongoClient()
    c = connection["comments"]
    
    CID = getcount("comments") + 1

    from datetime import datetime
    result = db.restaurants.insert_one(
        {
            "title": t,
            #"BID": ID,
            "username": un,
            "post": post
            #(still gotta figure out date stuff) "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
        }
    )


    
    TEMPLATE = "INSERT INTO comments VALUES(%(CID)s, %(BID)s, \"%(username)s\", \"%(comment)s\");" 
    q = TEMPLATE%({"CID":CID, "BID":BID, "username":un, "comment":cmt})
    c.execute(q)

    connection.commit()
    connection.close()

def getblogs(start, end):
    #returns list of blogs with IDs from start to end
    connection = MongoClient()
    c = connection["blogs"]
    
    TEMPLATE = "SELECT * FROM blogs WHERE BID >= %(st)s AND BID <= %(end)s"
    q = TEMPLATE%({"st":start, "end":end})
    result = c.execute(q)
    bloglist = []
    for row in result:
        bloglist.append(row)
    return bloglist

def getoneblog (BID):
    #displays the blog whose blog ID matches BID
    connection = MongoClient()
    c = connection["blogs"]

    TEMPLATE = "SELECT * FROM blogs WHERE BID = %(blogid)s"
    q = TEMPLATE%({"blogid":BID})
    result=c.execute(q)
    
    bloginfo = []
    for data in result:
        bloginfo.append(data)
    return bloginfo

def getblogcomments (BID):
    #displays the comments whose CID matches BID
    connection = MongoClient()
    c = connection["blogs"]

    TEMPLATE = "SELECT comments.username, comments.comment FROM comments WHERE BID = %(blogid)s"
    q = TEMPLATE%({"blogid":BID})
    result=c.execute(q)
    
    commentinfo = []
    for data in result:
        commentinfo.append(data)
    return commentinfo

def getcount(source):
    connection = MongoClient()
    c = connection["blogs"]

    TEMPLATE = "SELECT COUNT(*) FROM %(source)s"
    q = TEMPLATE%({"source" : source})
    result = c.execute(q)
    for data in result:
        return data[0]
