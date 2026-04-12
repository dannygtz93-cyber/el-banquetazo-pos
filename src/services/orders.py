from datetime import datetime
from src.database.db import get_connection


def crear_orden():
    conn = get_connection()
    cursor = conn.cursor()

    # Obtener último número
    cursor.execute("SELECT MAX(numero) FROM orders")
    result = cursor.fetchone()[0]

    numero = (result or 0) + 1

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO orders (numero, fecha)
        VALUES (?, ?)
    """, (numero, fecha))

    conn.commit()

    order_id = cursor.lastrowid

    conn.close()

    return order_id


def obtener_ordenes_abiertas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM orders
        WHERE estado = 'abierta'
        ORDER BY numero DESC
    """)

    ordenes = cursor.fetchall()

    conn.close()

    return ordenes


def agregar_producto(order_id, product_id, cantidad=1):
    conn = get_connection()
    cursor = conn.cursor()

    # Obtener precio producto
    cursor.execute("""
        SELECT precio FROM products
        WHERE id = ?
    """, (product_id,))

    producto = cursor.fetchone()

    if not producto:
        return

    precio = producto["precio"]

    cursor.execute("""
        INSERT INTO order_items (order_id, product_id, cantidad, precio)
        VALUES (?, ?, ?, ?)
    """, (order_id, product_id, cantidad, precio))

    conn.commit()
    conn.close()

    calcular_total(order_id)


def obtener_items_orden(order_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            order_items.id,
            products.nombre,
            order_items.cantidad,
            order_items.precio
        FROM order_items
        JOIN products ON products.id = order_items.product_id
        WHERE order_items.order_id = ?
    """, (order_id,))

    items = cursor.fetchall()

    conn.close()

    return items


def calcular_total(order_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(cantidad * precio) as total
        FROM order_items
        WHERE order_id = ?
    """, (order_id,))

    total = cursor.fetchone()["total"] or 0

    cursor.execute("""
        UPDATE orders
        SET total = ?
        WHERE id = ?
    """, (total, order_id))

    conn.commit()
    conn.close()

    return total


def cerrar_orden(order_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE orders
        SET estado = 'cerrada'
        WHERE id = ?
    """, (order_id,))

    conn.commit()
    conn.close()