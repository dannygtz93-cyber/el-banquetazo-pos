import flet as ft


def main_view(page: ft.Page):

    return ft.View(
        route="/main",
        controls=[
            ft.Row(
                expand=True,
                controls=[

                    # Productos
                    ft.Container(
                        expand=3,
                        padding=10,
                        content=ft.Column(
                            expand=True,
                            controls=[
                                ft.Text(
                                    "Productos",
                                    size=20,
                                    weight=ft.FontWeight.BOLD
                                ),

                                ft.GridView(
                                    expand=True,
                                    runs_count=3,
                                    spacing=10,
                                    run_spacing=10,
                                    controls=[
                                        ft.ElevatedButton("Taco Asada"),
                                        ft.ElevatedButton("Taco Pastor"),
                                        ft.ElevatedButton("Quesadilla"),
                                    ]
                                )
                            ]
                        )
                    ),

                    # Orden actual
                    ft.Container(
                        expand=2,
                        padding=10,
                        bgcolor=ft.Colors.GREY_100,
                        content=ft.Column(
                            expand=True,
                            controls=[
                                ft.Text(
                                    "Orden Actual",
                                    size=20,
                                    weight=ft.FontWeight.BOLD
                                ),

                                ft.ListView(
                                    expand=True,
                                    controls=[
                                        ft.Text("Taco Asada - $25"),
                                    ]
                                ),

                                ft.ElevatedButton(
                                    "Cobrar",
                                    height=60
                                )
                            ]
                        )
                    ),

                    # Órdenes abiertas
                    ft.Container(
                        expand=1,
                        padding=10,
                        content=ft.Column(
                            expand=True,
                            controls=[
                                ft.Text(
                                    "Órdenes",
                                    size=20,
                                    weight=ft.FontWeight.BOLD
                                ),

                                ft.ListView(
                                    expand=True,
                                    controls=[
                                        ft.ElevatedButton("Orden #1"),
                                        ft.ElevatedButton("Orden #2"),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        ]
    )