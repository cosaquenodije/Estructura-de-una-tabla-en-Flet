import flet as ft

def show_popup(page: ft.Page, title: str, message: str):
    page.open(ft.AlertDialog(title=ft.Text(title), content=ft.Text(message)))

def show_popup_auto_close(page: ft.Page, message: str):
    page.open(ft.SnackBar(ft.Text(message)))

def show_snackbar(page: ft.Page, message: str):
    page.open(ft.SnackBar(ft.Text(message)))

def confirm_dialog(page: ft.Page, message: str, on_confirm):
    page.open(ft.AlertDialog(
        title=ft.Text("Confirmar"),
        content=ft.Text(message),
        actions=[
            ft.TextButton("Sí", on_click=lambda e: on_confirm()),
            ft.TextButton("No", on_click=lambda e: page.close(page.dialog))
        ]
    ))