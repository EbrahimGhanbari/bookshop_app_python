import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)" )
        self.conn.commit()
        

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows=self.cur.fetchall()
        return rows

    def drop(self):
        self.cur.execute("DROP TABLE books")
        self.conn.commit()

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? or year=? OR isbn=?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id=?", (id, ))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



# insert("The earth", "John smith", 1989, 13824614)
# print(search(author="John smith"))
# delete(3)
# update(1, "The moon", "Dicken Club", 1917, 6105715)
# print(view()) 
