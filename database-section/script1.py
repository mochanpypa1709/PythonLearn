import sqlite3

def create_table():
    conn = sqlite3.connect("database-section/lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, qty, price):
    conn = sqlite3.connect("database-section/lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, qty, price))
    conn.commit()
    conn.close()

#create_table()
insert("Kopi", 5, 18)

def view():
    conn = sqlite3.connect("database-section/lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())