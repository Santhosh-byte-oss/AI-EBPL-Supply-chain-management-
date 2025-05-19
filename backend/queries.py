from backend.db import get_connection

def fetch_inventory_status():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    rows = cur.fetchall()
    conn.close()
    return rows

def fetch_low_stock_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory WHERE stock < reorder_level")
    rows = cur.fetchall()
    conn.close()
    return rows
