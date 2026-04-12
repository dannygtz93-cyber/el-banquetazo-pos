import flet as ft


def cash_view(page: ft.Page):

    return ft.View(
        "/cash",
        controls=[
            ft.Column(
                alignment="center",
                horizontal_alignment="center",
                expand=True,
                controls=[

                    ft.Text(
                        "Caja Cerrada",
                        size=30,
                        weight="bold"
                    ),

                    ft.TextField(
                        label="Fondo inicial",
                        width=300
                    ),

                    ft.ElevatedButton(
                        "Abrir Caja",
                        width=200,
                        height=50
                    )

                ]
            )
        ]
    )