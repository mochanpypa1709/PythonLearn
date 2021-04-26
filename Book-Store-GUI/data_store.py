import sqlite3

def connect():
    conn = sqlite3.connect("Book-Store-GUI/books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("Book-Store-GUI/books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Book-Store-GUI/books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("Book-Store-GUI/books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(qyt,price,item):
    conn = sqlite3.connect("Book-Store-GUI/books.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (qyt,price,item))
    conn.commit()
    conn.close()

connect()
#insert("Kopi", 5, 18)
#delete("Kopi")
#update(6,20,"Kopi")
#print(view())