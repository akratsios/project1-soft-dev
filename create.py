import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()
q = "CREATE TABLE users (username text, password text)"
c.execute(q)

conn.commit()
