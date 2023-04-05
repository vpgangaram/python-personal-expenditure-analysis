import sqlite3


db_local = 'expenses.db'


conn = sqlite3.connect(db_local)


c = conn.cursor()

c.execute("""
SELECT * FROM anlysis
""")

expens_info = c.fetchall()

for e in expens_info:
    print(e)

conn.commit()
conn.close()