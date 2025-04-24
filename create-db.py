import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('john', 'doe')")
cursor.execute("INSERT INTO users (username, password) VALUES ('alice', 'alice123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('paul', 'p4$$l')")
conn.commit()
conn.close()
