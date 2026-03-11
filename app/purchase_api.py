from fastapi import APIRouter
from pydantic import BaseModel
from app.database import save_purchase
from app.gold_price import get_gold_price

router = APIRouter()

class Purchase(BaseModel):
    user: str
    amount: int


@router.post("/buy-gold")
def buy_gold(purchase: Purchase):

    price_per_gram = get_gold_price()

    grams = purchase.amount / price_per_gram

    save_purchase(purchase.user, purchase.amount, grams)

    return {
        "status": "success",
        "gold_price_per_gram": price_per_gram,
        "amount_invested": purchase.amount,
        "gold_purchased_grams": round(grams,5),
        "message": f"{purchase.user} successfully purchased digital gold."
    }