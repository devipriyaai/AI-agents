from flask import Flask, request, render_template_string

app = Flask(__name__)

faq = {
    "price": "Our sarees start from ₹399.",
    "cod": "Cash on Delivery is not available.",
    "shipping": "Shipping charges depend on location. Tamil Nadu ₹40, Other states ₹60.",
    "saree": "We have Kalyani Cotton and Soft Silk sarees."
}

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Customer support AI Agent</title>
</head>
<body style="font-family: Arial; padding: 40px;">
    <h2> Saree Shop – Customer support AI Agent</h2>

    <form method="post">
        <input type="text" name="user_input" placeholder="Ask your question..." size="45" required>
        <br><br>
        <button type="submit">Send</button>
    </form>

    {% if user %}
        <p><b>You:</b> {{ user }}</p>
        <p><b>AI Agent:</b> {{ response }}</p>
    {% endif %}
</body>
</html>
"""

def faq_response(user_text):
    text = user_text.lower()

    for key in faq:
        if key in text:
            return faq[key]

    if "exit" in text or "bye" in text:
        return "Thank you for visiting  Have a nice day!"

    return "Please ask about price, COD, shipping, or saree availability."


@app.route("/", methods=["GET", "POST"])
def home():
    user = ""
    response = ""

    if request.method == "POST":
        user = request.form["user_input"]
        response = faq_response(user)

    return render_template_string(HTML_PAGE, user=user, response=response)


if __name__ == "__main__":
    app.run(debug=True)
