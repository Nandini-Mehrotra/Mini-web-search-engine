import sqlite3

conn = sqlite3.connect("search_engine.db")

cursor = conn.cursor()

cursor.execute("SELECT title, url FROM pages")

rows = cursor.fetchall()

for row in rows:
    print("\nTITLE:", row[0])
    print("URL:", row[1])

conn.close()