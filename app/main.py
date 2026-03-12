from fastapi import FastAPI
from app.chat_api import router as chat_router
from app.purchase_api import router as purchase_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI(title="Gold Investment AI API")

app.include_router(chat_router)
app.include_router(purchase_router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def home():
    return FileResponse("app/static/index.html")