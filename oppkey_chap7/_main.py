from fastapi import FastAPI
from app.api import register_routes
from app.ui import build_ui
import flet as ft
import flet_fastapi

def main(page:ft.Page):
    build_ui(page)

app=FastAPI()
register_routes(app)
flet_app=flet_fastapi.app(main)
app.mount("/", flet_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8550)