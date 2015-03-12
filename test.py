#coding:utf8
import sqlite3

db_name = "doubanbookID.db"
conn = sqlite3.connect(db_name)
cur = conn.cursor()

cur.execute("select * from bookid where id = 1000001")

row = cur.fetchone()

print row[0],row[1].encode('utf8','ignore').replace("\\/","\\")

conn.close()
