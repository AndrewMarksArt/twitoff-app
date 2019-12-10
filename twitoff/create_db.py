import sqlite3


conn = sqlite3.connect('my_db.sqlite')
cur = conn.cursor()
cur.execute("""
DROP TABLE IF EXISTS users;
""")
conn.commit()
