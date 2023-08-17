from fastapi import FastAPI
from .routers.items import items_router

def create_app():
    app = FastAPI()
    app.include_router(items_router)
    return app