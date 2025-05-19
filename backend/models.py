import sqlite3

DB_PATH = "supply_chain.db"

def create_inventory_table():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            reorder_level INTEGER NOT NULL,
            supplier TEXT,
            last_updated TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_inventory(product_name, quantity, reorder_level, supplier, last_updated):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO inventory (product_name, quantity, reorder_level, supplier, last_updated)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_name, quantity, reorder_level, supplier, last_updated))
    conn.commit()
    conn.close()

def fetch_inventory_status():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    rows = cur.fetchall()
    conn.close()
    return rows

def fetch_low_stock_items():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory WHERE quantity <= reorder_level")
    rows = cur.fetchall()
    conn.close()
    return rows
