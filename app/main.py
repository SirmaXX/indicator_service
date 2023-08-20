from fastapi import FastAPI
from .routers.items import items_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse

def create_app():
    app = FastAPI()
    templates = Jinja2Templates(directory="app/templates")
    app.include_router(items_router)
    return app