from transformers import pipeline

# Load FREE AI model
ai_model = pipeline("text-generation", model="distilgpt2")

# Rule-based FAQ
faq = {
    "price": "Our sarees start from ₹399.",
    "cod": "Cash on Delivery is not available.",
    "shipping": "Shipping charges depend on location.",
    "saree": "We have Cotton and Semi Silk sarees."
}

def check_faq(question):
    question = question.lower()
    for key in faq:
        if key in question:
            return faq[key]
    return None

print("AI Customer Support Chatbot")
print("Type 'exit' to stop")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Thank you")
        break

    faq_answer = check_faq(user_input)

    if faq_answer:
        print("Bot:", faq_answer)
    else:
        response = ai_model(
            user_input,
            max_length=60,
            num_return_sequences=1
        )
        print("Bot:", response[0]["generated_text"])
