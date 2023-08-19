from fastapi import APIRouter,Request
from pydantic import BaseModel
import joblib
import numpy as np

loaded_model = joblib.load('../../models/trained_model.pkl')

items_router = APIRouter()


@items_router.get("/health",description="servisin çalışıp çalışmadığını kontrol eden router")
async def health(req: Request): 
    health=True
    if health==True:
        return True
    else:
        return None



@items_router.get("/",description="index için router")
async def api_index():
    """ 
    iş servisinin giriş sayfası
    """
    return {"Hello": "Job"}


class Item(BaseModel):
    features: list

@items_router.post("/predict/")
def predict(item: Item):
    features = np.array(item.features).reshape(1, -1)  # Ensure proper shape for prediction
    prediction = loaded_model.predict(features)
    return {"prediction": int(prediction[0])}