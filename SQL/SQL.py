import sqlite3

con = sqlite3.connect('tutorial.db')

cur = con.cursor()

res = cur.execute("SELECT title, year, score FROM movie WHERE year = 1987 OR score = 9.4")

for i in res.fetchall():
    print(i)

con.commit()

con.close()