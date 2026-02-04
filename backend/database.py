import sqlite3
from typing import Optional, TypedDict

class User(TypedDict):
  name: str
  gmail: str
  password: bytes

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def drop_users():
  cursor.execute('DROP TABLE users')

cursor.execute("""
  CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 gmail TEXT,
                 password BLOB)  
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

def retrive_data(gmail: str) -> Optional[User]:
  with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT name, gmail, password FROM users WHERE gmail = ?',
                   (gmail,))
    row: tuple = cursor.fetchone()
    if row:
      name, gmail, password = row
      return {'name': name, 'gmail': gmail, 'password': password}
    return None