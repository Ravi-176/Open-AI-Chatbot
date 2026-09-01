# 📚 NoteBot

NoteBot is a simple **PDF-based AI chatbot** built with **Streamlit**.
It allows users to upload their notes in PDF format and ask questions about the uploaded content.

The application uses **Hugging Face embeddings** and **FAISS** for finding relevant information from the PDF, and an **OpenRouter LLM** to generate answers.

## 🚀 Features

* Upload PDF notes
* Extract text from PDF files
* Split PDF content into smaller chunks
* Generate embeddings using Hugging Face
* Store embeddings using FAISS
* Perform similarity search for user questions
* Generate answers using an OpenRouter AI model
* Simple and interactive Streamlit interface

## 🛠️ Technologies Used

* Python
* Streamlit
* PyPDF2
* LangChain
* Hugging Face
* FAISS
* OpenRouter
* Sentence Transformers

## 🔄 How It Works

```text
Upload PDF
    ↓
Extract Text
    ↓
Split Text into Chunks
    ↓
Generate Hugging Face Embeddings
    ↓
Store Embeddings in FAISS
    ↓
User Asks a Question
    ↓
Similarity Search
    ↓
Retrieve Relevant PDF Chunks
    ↓
Send Context to OpenRouter LLM
    ↓
Generate Answer
```

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/NoteBot.git
cd NoteBot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

NoteBot uses an OpenRouter API key.

Create the following file:

```text
.streamlit/secrets.toml
```

Add your API key:

```toml
OPEN_ROUTER_API_KEY = "your-api-key-here"
```

**Do not commit `secrets.toml` to GitHub.**

Make sure `.gitignore` contains:

```gitignore
.venv/
.streamlit/
__pycache__/
*.pyc
```

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💬 How to Use

1. Open NoteBot.
2. Upload a PDF containing your notes.
3. Enter a question related to the uploaded notes.
4. NoteBot searches the PDF for relevant information.
5. The AI generates an answer based on the retrieved content.

## 🧠 Embedding Model

The project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

This model converts text into numerical vectors that can be stored and searched using FAISS.

## 🤖 AI Model

The chatbot uses an OpenRouter-compatible model:

```text
openai/gpt-oss-20b
```

OpenRouter is accessed through LangChain's `ChatOpenAI` integration.

## 📁 Project Structure

```text
NoteBot/
│
├── .streamlit/
│   └── secrets.toml
│
├── .venv/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

> `.venv` and `.streamlit` should not be pushed to GitHub.

## 🎯 Project Purpose

This project was created as a beginner-friendly introduction to **Generative AI, RAG (Retrieval-Augmented Generation), embeddings, vector databases, and LangChain**.

## 🔮 Future Improvements

* Support multiple PDF files
* Add chat history
* Improve the UI
* Add source/document references to answers
* Add different AI models
* Store uploaded documents for later use
* Improve error handling for unsupported PDFs

## 👨‍💻 Author

**Somesh Ravi**

Built as a learning project while exploring **GenAI, LangChain, Python, and Streamlit**.
