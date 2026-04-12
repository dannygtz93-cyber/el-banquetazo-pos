import flet as ft


def config_view(page: ft.Page):

    return ft.View(
        route="/config",
        controls=[

            ft.Column(
                expand=True,
                padding=20,
                controls=[

                    ft.Text(
                        "Configuración Productos",
                        size=25,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.ListView(
                        expand=True,
                        spacing=10,
                        controls=[

                            ft.ListTile(
                                title=ft.Text("Taco Asada"),
                                trailing=ft.Row(
                                    width=200,
                                    alignment=ft.MainAxisAlignment.END,
                                    controls=[
                                        ft.IconButton(ft.Icons.EDIT),
                                        ft.Switch(),
                                        ft.IconButton(ft.Icons.DELETE),
                                    ]
                                )
                            )

                        ]
                    ),

                    ft.ElevatedButton(
                        "Agregar Producto"
                    )

                ]
            )

        ]
    )