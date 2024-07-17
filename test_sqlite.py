import sqlite3

# Test creating a connection
conn = sqlite3.connect('test.db')
conn.close()

print("SQLite3 is installed and working!")
