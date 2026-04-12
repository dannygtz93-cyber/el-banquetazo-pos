import flet as ft


def config_view(page: ft.Page):

    return ft.View(
        "/config",
        controls=[

            ft.Column(
                expand=True,
                controls=[

                    ft.Text(
                        "Configuración Productos",
                        size=25,
                        weight="bold"
                    ),

                    ft.ListView(
                        expand=True,
                        controls=[

                            ft.ListTile(
                                title=ft.Text("Taco Asada"),
                                trailing=ft.Row(
                                    width=200,
                                    controls=[
                                        ft.IconButton(ft.icons.EDIT),
                                        ft.Switch(),
                                        ft.IconButton(ft.icons.DELETE),
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