import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

sval = "sval1"
jednotka = "mv"

cur.execute(f"SELECT {sval}_{jednotka} FROM {sval}")
cislo_vzorce = cur.fetchone()


cur.execute(f"SELECT * FROM {sval}_{jednotka} WHERE id IN ({int(cislo_vzorce[0])})")
rows = cur.fetchall()

print(f"{rows[0][1]} {rows[0][2]}")