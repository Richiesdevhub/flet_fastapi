import fastapi

_orig_init = fastapi.FastAPI.__init__

def _patched_init(self, *args, openapi_prefix=None, **kwargs):
    if openapi_prefix:
        kwargs.setdefault("root_path", openapi_prefix)
    _orig_init(self, *args, **kwargs)

fastapi.FastAPI.__init__ = _patched_init


from contextlib import asynccontextmanager

from fastapi import FastAPI
import flet as ft
import flet.fastapi as flet_fastapi

from app.api import register_routes
from app.ui import build_ui


async def main(page: ft.Page):
    build_ui(page)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()


app = FastAPI(lifespan=lifespan)
register_routes(app)

# Va al final: un mount en "/" captura todo lo que no esté definido antes
app.mount("/", flet_fastapi.app(main))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8550)