import flet as ft

def text_field(label, hint_text=None, prefix_icon=None, suffix_icon=None, on_change=None):
    return ft.TextField(
        label=label,
        width=400,
        height=50, 
        hint_text=hint_text,
        prefix_icon=prefix_icon,
        suffix_icon=suffix_icon,
        on_change=on_change,
        autofocus=True,
        autocorrect=True,
    )