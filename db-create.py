import sqlite3


db_local = 'expenses.db'


conn = sqlite3.connect(db_local)


c = conn.cursor()

c.execute("""
CREATE TABLE anlysis(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exp NUMBER,
    catg TEXT,
    date TEXT,
    desc TEXT
)
""")

conn.commit()
conn.close()