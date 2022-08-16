import pandas as pd
import os
import sqlite3

conn = sqlite3.connect('wiigolf.db')

conn.execute('''CREATE TABLE if not exists MATCHES("PLAYERA", "PLAYERB", "SCOREA", "SCOREB", "WINNER")''')

conn.execute("INSERT INTO MATCHES (PLAYERA, PLAYERB, SCOREA, SCOREB, WINNER) VALUES ('tk','brett','64','65','tk')")

c = conn.cursor()
c.execute("SELECT * FROM MATCHES WHERE WINNER = 'tk'")
print(c.fetchall())

conn.commit()
conn.close()
