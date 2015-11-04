from pymongo import MongoClient
import md5

#checks if username + password matches one in database
#if not, add username + password to database

        
def checkuser(username,password):
    connection = MongoClient()
    db = connection['blogProj']
    people = db.users
    m= md5.new()
    m.update(password)
    password = m.hexdigest()
    if (people.find({"user": username}).count() == 0):
        return "No Such User"
    else:
        if (people.find({"user": username, "pass": password}).count() == 0):
            return "Wrong Password"
        else:
            return "in"


def adduser(uname,passwd):
    if (checkuser(uname, "") == "No Such User"):
        connection = MongoClient()
        db = connection['blogProj']
        people = db.users
        m= md5.new()
        m.update(passwd)
        password = m.hexdigest()
        newUser = {"user": uname, "pass": password}
        people.insert(newUser)
        return "User Created"
    else:
        return "Username Taken"
        
     

