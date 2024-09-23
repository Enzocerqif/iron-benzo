import flet as ft

def button(text, on_click):
    return ft.ElevatedButton(
        text=text,
        on_click=on_click,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=30)),
        width=400,
    )
