import langchain_community
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import langchain_text_splitters
import streamlit as st
import ollama

#LOAD PDF 
loader = langchain_community.document_loaders.pdf.PyPDFLoader("Understanding_Mental_Health.pdf")
documents = loader.load()

#SPLIT PDF
text_splitter = langchain_text_splitters.CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

#CREATE EMBEDDINGS
embeddings = HuggingFaceEmbeddings()
db = FAISS.from_documents(texts, embeddings)

print("PDF loaded and embeddings created! (Type 'exit' to quit)")

while True:
    query = input("You:")
    if query.lower() == 'exit':
       break

    docs = db.similarity_search(query)
    context = "\n".join([doc.page_content for doc in docs])

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "Answer ONLY from the provided context. If the answer is not in the context, say 'I don't know'." },
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ]
    )
    print(f"Bot: {response['message']['content']}")