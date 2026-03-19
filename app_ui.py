import streamlit as st
import ollama

st.title("🧠 Echominds AI")

# Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Echominds AI, a helpful and friendly assistant."}
    ]

# Show chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"👤 You: {msg['content']}")
    elif msg["role"] == "assistant":
        st.write(f"🤖 Bot: {msg['content']}")

# Input + button (IMPORTANT)
user_input = st.text_input("Type your message")
if st.button("Send"):

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = ollama.chat(
            model="llama3",
            messages=st.session_state.messages
        )

        bot_reply = response['message']['content']

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})