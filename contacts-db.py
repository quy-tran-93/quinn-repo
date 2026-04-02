#!/usr/bin/env python3
import pymysql

print("Content-Type: text/html\n")

conn = pymysql.connect(host="localhost", user="quinn", password="123456", database="contacts_db")
cur = conn.cursor()

cur.execute("SELECT name, telephone FROM contacts")

print("<html><body><ul>")
for row in cur.fetchall():
    print(f"<li>{row[0]} : {row[1]}</li>")
print("</ul></body></html>")

conn.close()
