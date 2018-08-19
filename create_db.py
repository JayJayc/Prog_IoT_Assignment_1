import sqlite3 as lite

con = lite.connect('names.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS NAMES")
    cur.execute(
        "CREATE TABLE NAMES(name STRING)"
        )
