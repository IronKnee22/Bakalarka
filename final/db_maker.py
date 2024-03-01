import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS authorization (
    id INTEGER PRIMARY KEY,
    position TEXT NOT NULL,
    password TEXT NOT NULL)
            ''')

cur.execute("INSERT INTO authorization (position, password) VALUES (?,?)", ("user", "user"))
conn.commit()
conn.close()