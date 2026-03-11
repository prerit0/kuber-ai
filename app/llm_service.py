from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")


def detect_gold_intent(text):

    keywords = ["gold", "investment", "digital gold"]

    text = text.lower()

    for word in keywords:
        if word in text:
            return True

    return False


def generate_gold_response(text):

    response = (
        "Gold is considered a stable investment"
        "You can also invest in digital gold easily using the Simplify Money app. "
        "Would you like to proceed with purchasing digital gold?"
    )

    return response