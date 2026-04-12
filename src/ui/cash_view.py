import flet as ft


def cash_view(page: ft.Page):

    return ft.View(
        route="/cash",
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[

                        ft.Text(
                            "Caja Cerrada",
                            size=30,
                            weight=ft.FontWeight.BOLD
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
            )
        ]
    )