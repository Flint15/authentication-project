import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def drop_users():
  cursor.execute('DROP TABLE users')

cursor.execute("""
  CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 gmail TEXT,
                 password TEXT)  
""")
#drop_users()
conn.commit()
conn.close()

def insert_data(name: str, gmail: str, password: bytes):
  with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
      'INSERT INTO users (name, gmail, password) VALUES (?, ?, ?)',
      (name, gmail, password)
    )
    conn.commit()
  
  return 'Data were saved succesfully :) '

def retrive_data(gmail: str, password: str):
  with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT name, gmail FROM users WHERE gmail = ?',
                   (gmail,))
    user = cursor.fetchone()
    if user:
      return f'User was found: {user}'
    else:
      return 'No user with that email'