#!/usr/bin/env python3

print("Content-Type: text/html\n")

with open("/var/www/html/contacts.txt") as f:
    lines = f.readlines()

print("<html><body><h2>Contacts</h2><ul>")
for line in lines:
    print(f"<li>{line}</li>")
print("</ul></body></html>")

