import streamlit as st
import requests
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import tempfile

st.title("📄 Chat with PDF (Echominds AI)")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name
        st.write(f"📂 Uploaded: {uploaded_file.name}")
    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split text
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    # Create vector DB (store in session)
    if "db" not in st.session_state:
        embeddings = HuggingFaceEmbeddings()
        st.session_state.db = FAISS.from_documents(texts, embeddings)

    st.success("PDF processed! Ask your questions 👇")

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat
    for msg in st.session_state.messages:
        if msg["role"] == "user":
           with st.chat_message("user"):
            st.write(msg["content"])
        else:
           with st.chat_message("assistant"):
            st.write(msg["content"])

    # Input
    user_input = st.chat_input("Ask something from PDF")

    if user_input:
        # Search relevant chunks
        docs = st.session_state.db.similarity_search(user_input, k=3)
        context = " ".join([doc.page_content for doc in docs])

        # Ask LLM
        try:
            res = requests.post(
                "http://127.0.0.1:11434/api/chat",
                json={
                    "model": "llama3",
                    "messages": [
                        {"role": "system", "content": "Answer ONLY from the context. If not found, say 'I don't know'."},
                        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {user_input}"}
                    ],
                    "stream": False
                }
            ).json()
            bot_reply = res.get('message', {}).get('content', "Error: No response")
        except Exception as e:
            bot_reply = f"Connection Error: {e}"

        # Save chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        st.rerun()