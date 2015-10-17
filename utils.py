import sqlite3

connection = sqlite3.connect("database.db")
c = connection.cursor()

def addpost(t, ID, un, post):
    #inserts new post into the blogs table
    TEMPLATE = "INSERT INTO blogs VALUES (\"%(title)s\", %(BID)s, \"%(username)s\", \"%(post)s\");"
    q=TEMPLATE%({"title":t, "BID":ID, "username":un, "post":post})
    print q

    #currently c.execute(q) is giving us an error
    c.execute(q)

c.execute("CREATE TABLE IF NOT EXISTS blogs (title TEXT, BID INTEGER, username TEXT, post TEXT)")
addpost("kek", 69, "RarestPepe", "hey everyone it's a me Mario")
c.execute("SELECT * FROM blogs")


