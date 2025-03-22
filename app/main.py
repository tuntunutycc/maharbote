from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from .fortune import get_fortune

app = FastAPI(
    title="Maharbote API",
    description="A fortune prediction API based on birth day",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class FortuneRequest(BaseModel):
    day: str
    aspect: Optional[str] = "general"

@app.get("/")
async def root():
    return FileResponse("app/static/index.html")

@app.post("/fortune")
async def get_fortune_prediction(request: FortuneRequest):
    prediction = get_fortune(request.day, request.aspect)
    return {
        "birth_day": request.day,
        "aspect": request.aspect,
        "prediction": prediction
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 