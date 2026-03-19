
# 🤖 AI PDF Chatbot (RAG)

An AI-powered chatbot that allows users to upload PDFs and ask questions based on the document content using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload and chat with PDF documents  
- 🧠 Context-aware responses using RAG  
- ⚡ Fast semantic search with FAISS  
- 🖥️ Interactive UI using Streamlit  
- 🔒 Runs locally using Ollama (no API cost)  

---

## 🛠️ Tech Stack

- Python  
- Ollama (LLM - Llama3)  
- LangChain  
- FAISS (Vector Database)  
- Streamlit (UI)  

---

## 📂 Project Structure

```
.
├── app.py
├── app_ui.py
├── pdf_chat.py
├── pdf_ui.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ai-pdf-chatbot-rag.git
cd ai-pdf-chatbot-rag
```

Create virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\Activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run pdf_ui.py
```

---

## 🧠 How it Works

1. PDF is loaded and split into chunks  
2. Text is converted into embeddings  
3. FAISS stores embeddings  
4. User query → similarity search  
5. Relevant context sent to LLM  
6. LLM generates accurate answer  

---

## 📌 Future Improvements

- Multi-PDF support  
- Voice assistant integration  
- Online deployment  
- Chat history persistence  

---

## 👨‍💻 Author

Pranav Karande
