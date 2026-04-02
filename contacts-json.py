#!/usr/bin/env python3
import pymysql
import json

print("Content-Type: application/json\n")

conn = pymysql.connect(host="localhost", user="quinn", password="123456", database="contacts_db")
cur = conn.cursor()

cur.execute("SELECT name, telephone FROM contacts")

data = [{"name": r[0], "telephone": r[1]} for r in cur.fetchall()]

print(json.dumps({
    "ok": True,
    "count": len(data),
    "data": data
}))

conn.close()
