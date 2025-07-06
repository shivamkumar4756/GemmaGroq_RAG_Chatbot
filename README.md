# 🤖 GemmaGroq Q&A Chatbot

> Ask questions from any website using LangChain, Cohere embeddings, and Groq-powered Gemma 2 LLM — via Retrieval-Augmented Generation (RAG)

---

## 🚀 Features

- 🔗 Enter any **website URL**
- 🧠 Uses **Cohere embeddings** for semantic understanding
- ⚡ Inference powered by **Groq’s Gemma 2 model** (`gemma2-9b-it`)
- 📚 Retrieval-Augmented Generation (RAG) using **LangChain**
- 🔍 Get highly relevant answers based on scraped content
- 🖥️ Simple and clean **Streamlit UI**

---

## 🏗️ Tech Stack

| Component       | Tool/Service                     |
|----------------|----------------------------------|
| UI             | Streamlit                        |
| LLM            | `gemma2-9b-it` via Groq           |
| Embeddings     | Cohere (`embed-english-v3.0`)    |
| Vector Store   | FAISS                            |
| Framework      | LangChain                        |
| Scraping       | WebBaseLoader + BeautifulSoup    |
| Deployment     | Streamlit Cloud (or local)       |

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/gemmagroq-rag-chatbot.git
cd gemmagroq-rag-chatbot
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the root directory:

```env
GROQ_API_KEY="your-groq-api-key"
COHERE_API_KEY="your-cohere-api-key"
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📄 `requirements.txt`

```txt
streamlit
langchain
langchain-community
langchain-groq
cohere
faiss-cpu
python-dotenv
beautifulsoup4
```

---

## 🧠 How It Works

1. User enters a URL → LangChain scrapes the page
2. Content is split into chunks
3. Cohere embeds the chunks
4. FAISS stores them for similarity search
5. User asks a question → relevant chunks retrieved
6. Gemma 2 (via Groq) generates the answer using LangChain RAG

---

## 🛠️ Future Ideas

- Support PDF/doc/file uploads
- Add memory for follow-up questions
- Multi-page website ingestion
- Display source URLs with answers

---

## ✍️ Author

**Shivam Kumar**  
B.Tech CSE | Google Cloud GenAI Intern  
[LinkedIn](#) | [GitHub](#)

---

## 📜 License

This project is licensed under the MIT License.
