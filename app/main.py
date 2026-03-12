from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.chat_api import router as chat_router
from app.purchase_api import router as purchase_router

app = FastAPI(title="Gold Investment AI API")

app.include_router(chat_router)
app.include_router(purchase_router)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Gold Investment AI</h1>
    <p>API is running successfully.</p>
    <p>Go to <a href='/docs'>API Documentation</a></p>
    """