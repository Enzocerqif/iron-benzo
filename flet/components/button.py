import flet as ft

def button(text, on_click, icon=None):
    return ft.ElevatedButton(
        text=text,
        on_click=on_click,
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(size=25, font_family="Roboto"),
            side=ft.BorderSide(color=ft.colors.WHITE, width=1)
        ),
        width=400,
        height=50,
        bgcolor=ft.colors.BLACK38,
        icon=icon,
    )
