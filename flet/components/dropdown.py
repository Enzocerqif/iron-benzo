import flet as ft

def dropdown(label, options = [], on_change=None):
    return ft.Dropdown(
        label=label,
        options=[ft.dropdown.Option(option) for option in options],
        width=400,
        height=50,
        on_change=on_change,
    )