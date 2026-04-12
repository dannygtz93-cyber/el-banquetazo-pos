from .db import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabla de órdenes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER,
        fecha TEXT,
        total REAL DEFAULT 0,
        estado TEXT DEFAULT 'abierta'
    )
    """)

    # Tabla productos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )
    """)

    # Tabla items de orden
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        product_id INTEGER,
        cantidad INTEGER DEFAULT 1,
        precio REAL,
        FOREIGN KEY(order_id) REFERENCES orders(id),
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
    """)

    conn.commit()
    conn.close()

def seed_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]

    if count == 0:
        productos = [
            ("Bistec", 30, "Tacos"),
            ("Longaniza", 30, "Tacos"),
            ("Pechuga", 30, "Tacos"),
            ("Chuleta", 30, "Tacos"),
            ("Campechano", 35, "Tacos"),
            ("Costilla", 35, "Tacos"),
            ("Arrachera", 35, "Tacos"),
            ("Especial con queso", 40, "Especial"),
            ("Refresco", 30, "Bebidas"),
        ]

        cursor.executemany("""
            INSERT INTO products (nombre, precio, categoria)
            VALUES (?, ?, ?)
        """, productos)

    conn.commit()
    conn.close()