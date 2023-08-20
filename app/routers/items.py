from fastapi import APIRouter,Request, Form
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.templating import Jinja2Templates
import os

templates = Jinja2Templates(directory="app/templates")

model_path = os.path.join(os.path.dirname(__file__), '../../models/diabet_012.pkl')
loaded_model = joblib.load(model_path)
print(model_path)

items_router = APIRouter()



@items_router.get("/",description="index için router")
async def api_index(request: Request):
     return templates.TemplateResponse("index.html", {"request": request})



@items_router.post('/predictform/',description="index için router")
async def formpredict(
    high_bp: int = Form(...),
    high_collestrol: int = Form(...),
    bmi: float = Form(...),
    gen_health:int = Form(...),
    diff_walk: int = Form(...),
):
    json= [high_bp,high_collestrol,bmi,gen_health,diff_walk]

    features = np.array(json).reshape(1, -1)  # Ensure proper shape for prediction
    prediction = loaded_model.predict(features)
    return {"prediction": int(prediction[0])}





@items_router.get("/health",description="servisin çalışıp çalışmadığını kontrol eden router")
async def health(req: Request): 
    health=True
    if health==True:
        return True
    else:
        return None


class Item(BaseModel):
    features: list

@items_router.post("/predict/")
def predict(item: Item):
    features = np.array(item.features).reshape(1, -1)  # Ensure proper shape for prediction
    prediction = loaded_model.predict(features)
    return {"prediction": int(prediction[0])}














