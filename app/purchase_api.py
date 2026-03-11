from fastapi import APIRouter
from pydantic import BaseModel
from app.database import save_purchase

router = APIRouter()

class Purchase(BaseModel):
    user: str
    amount: int


@router.post("/buy-gold")
def buy_gold(purchase: Purchase):

    save_purchase(purchase.user, purchase.amount)

    return {
        "status": "success",
        "message": f"{purchase.user} purchased ₹{purchase.amount} worth of digital gold successfully."
    }