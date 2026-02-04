import requests

url = "http://127.0.0.1:5000/chat"

print("Type 'exit' to stop")

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break

    response = requests.post(url, json={"message": msg})
    print("Bot:", response.json()["reply"])
