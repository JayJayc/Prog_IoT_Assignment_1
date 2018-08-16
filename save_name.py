import sqlite3

dbname = "names.db"
conn=sqlite3.connect(dbname)
curs=conn.cursor()
curs.execute("""INSERT INTO NAMES ('name') values ('JayJayC')""")
conn.commit()
conn.close()