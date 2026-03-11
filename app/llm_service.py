from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")


def detect_gold_intent(text):

    keywords = ["gold", "investment", "digital gold"]

    text = text.lower()

    for word in keywords:
        if word in text:
            return True

    return False


def generate_gold_response(text):

    prompt = f"""
    User question: {text}

    Answer the question briefly about gold investment.
    Then suggest that the user can invest in digital gold using the Simplify Money app.
    """

    output = generator(prompt, max_length=80)

    return output[0]["generated_text"]