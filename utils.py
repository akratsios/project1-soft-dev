import random
from pymongo import MongoClient
import time

def addblog(t, un, post):    
    #inserts new blog into the blogs table
    connection = MongoClient()
    db = connection["blogProj"]
    c = db.blogs

    ID = getcount("blogs") + 1

    D = time.strftime("%x %X")

    c.insert_one(
        {
            "title": t,
            "BID": ID,
            "username": un,
            "post": post,
            "date": D
        }
    )
    

def addcomment(BID, un, cmt):
    #inserts new comment into the comments table
    connection = MongoClient()
    db = connection["blogProj"]
    c = db.comments
    
    CID = getcount("comments") + 1

    D = time.strftime("%x %X")

    c.insert_one(
        {
            "CID":CID, 
            "BID":BID, 
            "username":un, 
            "comment":cmt,
            "date": D
        }
    )


def getblogs(start, end):
    #returns list of blogs with IDs from start to end
    connection = MongoClient()
    db = connection["blogProj"]
    c = db.blogs
    #TEMPLATE = "SELECT * FROM blogs WHERE BID >= %(st)s AND BID <= %(end)s"
    #q = TEMPLATE%({"st":start, "end":end})
    result = c.find( { "BID": { '$gte': start }, "BID" :{ '$lte': end }})
    bloglist = []
    for row in result:
        bloglist.append(row)
    return bloglist

def getoneblog (BID):
    #displays the blog whose blog ID matches BID
    connection = MongoClient()
    db = connection["blogProj"]
    c = db.blogs

    #TEMPLATE = "SELECT * FROM blogs WHERE BID = %(blogid)s"
    #q = TEMPLATE%({"blogid":BID})
    result = c.find("BID")
    
    bloginfo = []
    for data in result:
        bloginfo.append(data)
    return bloginfo

def getblogcomments (BID):
    #displays the comments whose CID matches BID
    connection = MongoClient()
    db = connection["blogProj"]
    c = db.comments

    #TEMPLATE = "SELECT comments.username, comments.comment FROM comments WHERE BID = %(blogid)s"
    #q = TEMPLATE%({"blogid":BID})
    result = c.find("BID")
    
    commentinfo = []
    for data in result:
        commentinfo.append(data)
    return commentinfo

def getcount(source):
    connection = MongoClient()
    db = connection["blogProj"]
    if (source == "comments"):
        c = db.comments
        result = c.count()
        return result
    else:
        c = db.blogs
        result = c.count()
        return result



