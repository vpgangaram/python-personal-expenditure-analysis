import sqlite3


db_local = 'expenses.db'


conn = sqlite3.connect(db_local)


c = conn.cursor()

c.execute("""
INSERT INTO anlysis(exp, catg, date, desc) VALUES
(1200, 'Fuel', '12-12-2022', 'hello'),
(100, 'Hotel', '15-12-2022', 'Hi')
""")

conn.commit()
conn.close()