import sqlite3

conn = sqlite3.connect("Chinook.db")
cur = conn.cursor()
'''
for row in cur.execute('Select * from Album;'):
    print row
'''
for row in cur.execute('Select Track.Name From Track Order by Track.Milliseconds DESC;'):
    print row
