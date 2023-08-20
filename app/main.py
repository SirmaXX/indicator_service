from fastapi import FastAPI
from .routers.items import items_router
from fastapi.templating import Jinja2Templates


def create_app():
    app = FastAPI(title="Diabet indicator", description="Diabet indicator estimator with %86 accuracy example app and api") 
    app.include_router(items_router)
    return app