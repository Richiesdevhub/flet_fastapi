import flet as ft

def build_ui(page: ft.Page):
    main_message=page.add(ft.Text("let plus FastAPI Demo", size=40),
                          ft.FilledButton("Button"))

    page.add(main_message)
