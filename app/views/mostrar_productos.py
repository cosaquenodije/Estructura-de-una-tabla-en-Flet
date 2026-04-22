import flet as ft
from typing import Any
from app.services.transacciones_api_productos import list_products
from app.styles.estilos import Colors, Textos_estilos

def products_view(page: ft.Page) -> ft.Control:
    columnas = [
        ft.DataColumn(label=ft.Text("Nombre", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Cantidad", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Ingreso", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Min", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Max", style=Textos_estilos.H4)),
    ]

    try:
        data = list_products(limit=200, offset=0)
        productos = data.get("productos", []) or []
    except Exception as ex:
        print(f"Error cargando productos: {ex}")
        productos = []

    filas = []
    for p in productos:
        filas.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(p.get("name", ""))),
                    ft.DataCell(ft.Text(str(p.get("quantity", "")))),
                    ft.DataCell(ft.Text(p.get("ingreso_date", "") or "")),
                    ft.DataCell(ft.Text(str(p.get("min_stock", "")))),
                    ft.DataCell(ft.Text(str(p.get("max_stock", "")))),
                ]
            )
        )

    tabla = ft.DataTable(
        columns=columnas,
        rows=filas,
        width=900,
        heading_row_height=60,
        heading_row_color=Colors.BG,
        data_row_max_height=60,
        data_row_min_height=48
    )

    #Regresa la tabla con los datos
    #return tabla

    total_text = ft.Text(f"Total de productos: {len(productos)}", style=Textos_estilos.H4)

    btn_nuevo = ft.ElevatedButton("Nuevo registro")

    #Se prepara un sistema de columnas para mostrar tanto el total de registros y
    #la tabla y con un mejor formato
    #Cuando se necesita el scroll tambien se muestra
    contenido = ft.Column(
        #Se crea un espacio entre cada elemento
        spacing=30,
        #Cuando no caben los elementos se genera el scroll
        scroll=ft.ScrollMode.AUTO,
        #Se establecen tanto el total como la tabla para mostrar
        ######## Se agrega el boton de nuevo registro ########
        controls=[btn_nuevo, total_text, ft.Container(content=tabla)]
    )
    #Se muestra esa columna
    return contenido
