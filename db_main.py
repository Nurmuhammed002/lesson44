import sqlite3

def create_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        size TEXT NOT NULL,
        price REAL NOT NULL,
        sku TEXT NOT NULL UNIQUE,
        photo_id TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sku TEXT NOT NULL,
        size TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        contact TEXT NOT NULL,
        FOREIGN KEY (sku) REFERENCES products (sku)
    )
    ''')

    conn.commit()
    conn.close()
