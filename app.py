import streamlit as st
import os 
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.document_loaders import WebBaseLoader
import cohere
from dotenv import load_dotenv
load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

st.title("GemmaGroq RAG Chatbot")

llm = ChatGroq(groq_api_key=groq_api_key, model="gemma2-9b-it")

prompt = ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}
"""
)

co = cohere.Client(COHERE_API_KEY)
class MyCohereEmbedder:
    def embed_documents(self, texts):
        response = co.embed(
            texts=texts,
            model="embed-english-v3.0",
            input_type="search_document"
        )
        return response.embeddings

    def embed_query(self, text):
        response = co.embed(
            texts=[text],
            model="embed-english-v3.0",
            input_type="search_query"
        )
        return response.embeddings[0]
    
    def __call__(self, text):
        return self.embed_query(text)

def vector_embeddings(user_url):
    if "vectors" not in st.session_state or st.session_state.get("last_url") != user_url:
        st.session_state.last_url = user_url
        st.session_state.embeddings = MyCohereEmbedder()
        st.session_state.loader = WebBaseLoader(user_url)  # Data Ingestion
        st.session_state.documents = st.session_state.loader.load()  # Documents Loading
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)  # Chunk Creation
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.documents)  # Splitting
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)  # Vector Embeddings

user_url = st.text_input("Enter the website URL to load content from")
prompt1 = st.text_input("Enter your question from documents")

if st.button("Documents Embeddings") and user_url:
    vector_embeddings(user_url)
    st.write("Vector Store DB is ready")

import time

if prompt1 and "vectors" in st.session_state:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    start = time.process_time()
    response = retrieval_chain.invoke({"input": prompt1})
    print("Response Time :", time.process_time() - start)
    st.write(response['answer'])

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")
