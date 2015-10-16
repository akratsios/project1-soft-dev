import sqlite3

connection = sqlite3.connect("database.db")
c = connection.cursor()

def addpost(t, ID, un, post):
    #inserts new post into the blogs table
    TEMPLATE = "INSERT INTO blogs VALUES ('%(title)s', %(BID)d, '%(username)', '%(post)');"
    q=TEMPLATE%({"title":t,"BID":ID,"username":un,"post":post})
    print q 

#def query():

addpost("kek", 69, "kirito", "hey everyone it's a me MArio")


