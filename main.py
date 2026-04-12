import flet as ft

from src.database.models import create_tables, seed_products
from src.ui.main_view import main_view


def main(page: ft.Page):

    # Configuración ventana
    page.title = "El Banquetazo POS"
    page.window_full_screen = True
    page.padding = 0

    # Inicializar base de datos
    create_tables()
    seed_products()

    # Agregar vista principal
    page.views.append(
        main_view(page)
    )

    page.update()


if __name__ == "__main__":
    ft.run(main)