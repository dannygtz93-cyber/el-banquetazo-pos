from src.database.models import create_tables, seed_products
from src.services.orders import crear_orden, agregar_producto

def test_orders():
    # Orden 1
    orden1 = crear_orden()
    agregar_producto(orden1, 1)
    agregar_producto(orden1, 2)

    # Orden 2
    orden2 = crear_orden()
    agregar_producto(orden2, 3)
    agregar_producto(orden2, 3)
    agregar_producto(orden2, 4)

    print("Ordenes creadas:", orden1, orden2)

def main():
    create_tables()
    seed_products()
    test_orders()

if __name__ == "__main__":
    main()