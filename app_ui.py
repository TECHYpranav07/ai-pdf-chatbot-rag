import streamlit as st
import requests

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

        try:
            res = requests.post(
                "http://127.0.0.1:11434/api/chat",
                json={
                    "model": "llama3",
                    "messages": st.session_state.messages,
                    "stream": False
                }
            ).json()
            bot_reply = res.get('message', {}).get('content', "Error: No response")
        except Exception as e:
            bot_reply = f"Connection Error: {e}"

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})