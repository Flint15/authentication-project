import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
  CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 gmail TEXT,
                 password TEXT)  
""")
conn.commit()
conn.close()

def insert_data(gmail: str, password: str):
  with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
      'INSERT INTO users (gmail, password) VALUES (?, ?)',
      (gmail, password)
    )
    conn.commit()
  
  return 'Data were saved succesfully :) '