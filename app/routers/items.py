from fastapi import APIRouter

items_router = APIRouter()

@items_router.get("/items/")
async def get_items():
    return [{"item_id": 1, "name": "Item 1"}, {"item_id": 2, "name": "Item 2"}]