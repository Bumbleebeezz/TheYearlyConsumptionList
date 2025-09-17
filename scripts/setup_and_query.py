import sqlite3

# Create (or connect to) the SQLite database
conn = sqlite3.connect("demo.db")
cur = conn.cursor()

# Create a table and insert some data
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cur.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
])

conn.commit()

# Query and print results
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

print("Users in database:")
for row in rows:
    print(row)

conn.close()