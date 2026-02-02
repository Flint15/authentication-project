import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT NOT NULL
  )      
''')
conn.commit()
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)",
               ('blue@example.com', 'veryhardohayopassword'))
