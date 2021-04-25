import mysql.connector

def create_table():
    conn = mysql.connector.connect(database="learnpython", user="root", password="", host="localhost")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, qty, price):
    conn = mysql.connector.connect(database="learnpython", user="root", password="", host="localhost")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item, qty, price))
    conn.commit()
    conn.close()

def view():
    conn = mysql.connector.connect(database="learnpython", user="root", password="", host="localhost")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = mysql.connector.connect(database="learnpython", user="root", password="", host="localhost")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(qyt,price,item):
    conn = mysql.connector.connect(database="learnpython", user="root", password="", host="localhost")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (qyt,price,item))
    conn.commit()
    conn.close()

create_table()
#insert("Alpukat Kocok", 3, 25)
#delete("Kopi")
update(10,30,"Susu")
print(view())