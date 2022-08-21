import pandas as pd
import os
import sqlite3

conn = sqlite3.connect('wiigolf.db')

#conn.execute('''CREATE TABLE if not exists ACCOUNTS("UNAME", "PASSWORD")''')

#conn.execute("INSERT INTO MATCHES (PLAYERA, PLAYERB, SCOREA, SCOREB, WINNER) VALUES ('tk','brett','64','65','tk')")
#conn.execute("INSERT INTO MATCHES (PLAYERA, PLAYERB, SCOREA, SCOREB, WINNER) VALUES ('tk','brett','62','64','tk')")
#conn.execute("INSERT INTO MATCHES (PLAYERA, PLAYERB, SCOREA, SCOREB, WINNER) VALUES ('tk','brett','60','62','tk')")
#conn.execute("INSERT INTO MATCHES (PLAYERA, PLAYERB, SCOREA, SCOREB, WINNER) VALUES ('tk','brett','57','66','tk')")
#conn.execute("INSERT INTO MATCHES (PLAYERA, PLAYERB, SCOREA, SCOREB, WINNER) VALUES ('tk','brett','61','58','brett')")
#conn.execute("INSERT INTO ACCOUNTS (UNAME, PASSWORD) VALUES ('test','garbage')")

c = conn.cursor()
c.execute("SELECT * FROM ACCOUNTS WHERE UNAME = 'test'")
print(c.fetchall())

conn.commit()
conn.close()
