import requests

print("This is Echominds AI, your personal assistant. How can I help you today? (Type 'exit' to quit)")

messages = [
    {"role": "system", "content": "You are Echominds AI, a helpful and friendly assistant."},
]

while True:
    user_input = input("You:")
    if user_input.lower() == 'exit':
       break    

    messages.append({"role": "user", "content": user_input})

    try:
        res = requests.post(
            "http://127.0.0.1:11434/api/chat",
            json={"model": "llama3", "messages": messages, "stream": False}
        ).json()
        bot_reply = res.get('message', {}).get('content', "Error: No response")
    except Exception as e:
        bot_reply = f"Connection Error: {e}"

    print("Bot:", bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})