from fastapi import APIRouter
from pydantic import BaseModel
from app.llm_service import detect_gold_intent, generate_gold_response

router = APIRouter()

class Query(BaseModel):
    message: str


@router.post("/chat")
def chat(query: Query):

    text = query.message.lower()

    # Detect purchase confirmation
    if text in ["yes", "yes please", "buy gold", "purchase gold"]:
        return {
            "type": "purchase_redirect",
            "response": "Great! Redirecting you to digital gold purchase.",
            "next_action": "/buy-gold"
        }

    # Detect gold investment questions
    if detect_gold_intent(text):

        response = generate_gold_response(text)

        return {
            "type": "gold_investment",
            "response": response,
            "next_action": "awaiting_user_confirmation"
        }

    return {
        "type": "general",
        "response": "I can help with gold investment related questions."
    }