import flet as ft


def reports_view(page: ft.Page):

    return ft.View(
        route="/reports",
        controls=[

            ft.Column(
                expand=True,
                padding=20,
                controls=[

                    ft.Text(
                        "Reporte de Ventas",
                        size=25,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Row(
                        spacing=20,
                        controls=[
                            ft.Card(
                                content=ft.Container(
                                    padding=20,
                                    content=ft.Text("Ventas Totales\n$2,500")
                                )
                            ),

                            ft.Card(
                                content=ft.Container(
                                    padding=20,
                                    content=ft.Text("Efectivo\n$1,200")
                                )
                            ),

                            ft.Card(
                                content=ft.Container(
                                    padding=20,
                                    content=ft.Text("Tarjeta\n$1,300")
                                )
                            ),
                        ]
                    ),

                ]
            )

        ]
    )