import flet as ft


def reports_view(page: ft.Page):

    return ft.View(
        "/reports",
        controls=[

            ft.Column(
                expand=True,
                controls=[

                    ft.Text(
                        "Reporte de Ventas",
                        size=25,
                        weight="bold"
                    ),

                    ft.Row(
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