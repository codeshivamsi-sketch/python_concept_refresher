import sqlite3

f = open("file.txt")
data = f.read() 
f.close() # if read() crashes, close() never runs




with open("file.txt") as f:
    data = f.read() # file always closed, even if read() crashes




# Works with anything that has __enter__ and __exit__ not just files
with sqlite3.connect("test.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO users (name) VALUES ('Shivam')")
    conn.commit()
# Connection closes automatically here.



# Query
with sqlite3.connect("test.db") as conn:
    result = conn.execute("SELECT * FROM users")
    for row in result:
        print(row)
# Connection closes automatically here.
