from fastapi import APIRouter
from pydantic import BaseModel
from app.llm_service import detect_gold_intent, generate_gold_response

router = APIRouter()

class Query(BaseModel):
    message: str

@router.post("/chat")
def chat(query: Query):

    text = query.message

    is_gold = detect_gold_intent(text)

    if is_gold:

        response = generate_gold_response(text)

        return {
            "type": "gold_investment",
            "response": response,
            "next_action": "buy_gold_api"
        }

    return {
        "type": "general",
        "response": "I can help with gold investment related questions."
    }