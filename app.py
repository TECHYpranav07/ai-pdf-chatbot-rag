import ollama

print("This is Echominds AI, your personal assistant. How can I help you today? (Type 'exit' to quit)")

messages = [
    {"role": "system", "content": "You are Echominds AI, a helpful and friendly assistant."},
]

while True:
    user_input = input("You:")
    if user_input.lower() == 'exit':
       break    

    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model = "llama3",
        messages=messages
    )
    print("Bot:", response['message']['content'])

    messages.append({"role": "assistant", "content": response['message']['content']})