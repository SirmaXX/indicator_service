from fastapi import FastAPI
from app.main import create_app
from config.settings import settings

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)