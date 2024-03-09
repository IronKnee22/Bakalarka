import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

# Vytvoření tabulky pro hesla + vložení
# cur.execute('''CREATE TABLE IF NOT EXISTS authorization (
#     id INTEGER PRIMARY KEY,
#     position TEXT NOT NULL,
#     password TEXT NOT NULL)
#             ''')
# cur.execute("INSERT INTO authorization (position, password) VALUES (?,?)", ("user", "user"))
# cur.execute("UPDATE authorization SET password = ? WHERE position = ?", ("8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918", "admin"))

# vytvoření tabulek pro převodní vzorce na jednotlivých svalech 

# cur.execute('''CREATE TABLE IF NOT EXISTS sval1_mm (
#                      id INTEGER PRIMARY KEY,
#                      sklon INTEGER NOT NULL,
#                      posun INTEGER NOT NULL,
#                      popis TEXT NOT NULL)
#                      ''')

# cur.execute('''CREATE TABLE IF NOT EXISTS sval1_mv (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval1_mbar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval1_mv2bar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')

# cur.execute('''CREATE TABLE IF NOT EXISTS sval2_mv (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval2_mbar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval2_mv2bar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')

# cur.execute('''CREATE TABLE IF NOT EXISTS sval3_mv (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval3_mbar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval3_mv2bar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval4_mv (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval4_mbar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')

# cur.execute('''CREATE TABLE IF NOT EXISTS sval4_mv2bar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval5_mv (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')
        
# cur.execute('''CREATE TABLE IF NOT EXISTS sval5_mbar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#                     ''')

# cur.execute('''CREATE TABLE IF NOT EXISTS sval5_mv2bar (
#                     id INTEGER PRIMARY KEY,
#                     sklon INTEGER NOT NULL,
#                     posun INTEGER NOT NULL,
#                     popis TEXT NOT NULL)
#  
#                    ''')

cur.execute('''CREATE TABLE IF NOT EXISTS sval5_mm (
                     id INTEGER PRIMARY KEY,
                     sklon INTEGER NOT NULL,
                     posun INTEGER NOT NULL,
                     popis TEXT NOT NULL)
                     ''')
cur.execute("INSERT INTO sval5_mm (sklon, posun, popis) VALUES (?,?,?)", (1, 1, "zakladni vzorec"))


cur.execute('''CREATE TABLE IF NOT EXISTS sval5(
                     id INTEGER PRIMARY KEY,
                     sval5_mm INTEGER NOT NULL,
                     sval5_mv INTEGER NOT NULL,
                     sval5_mbar INTEGER NOT NULL,
                     sval5_mv2bar INTEGER NOT NULL)
                     ''')
cur.execute("INSERT INTO sval5 (sval5_mm, sval5_mv, sval5_mbar, sval5_mv2bar) VALUES (?,?,?,?)", (1, 1, 1, 1))


conn.commit()
conn.close()