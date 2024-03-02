import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS authorization (
#     id INTEGER PRIMARY KEY,
#     position TEXT NOT NULL,
#     password TEXT NOT NULL)
#             ''')
# cur.execute("INSERT INTO authorization (position, password) VALUES (?,?)", ("user", "user"))
cur.execute("UPDATE authorization SET password = ? WHERE position = ?", ("8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918", "admin"))



conn.commit()
conn.close()