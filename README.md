# 🎥 YouTube RAG Chatbot

A Retrieval-Augmented Generation (RAG) application built with **LangChain**, **OpenAI**, and **FAISS** that allows users to ask questions about a YouTube video and receive answers grounded in the video's transcript.

---

## 🚀 Features

* Extract transcripts directly from YouTube videos
* Split long transcripts into manageable chunks
* Generate embeddings using OpenAI Embeddings
* Store embeddings in a FAISS vector database
* Retrieve relevant context based on user queries
* Generate context-aware answers using GPT models
* Summarize video content
* Prevent hallucinations by restricting answers to retrieved context

---

## 🛠️ Tech Stack

* Python
* LangChain
* OpenAI
* FAISS
* YouTube Transcript API
* Runnable Chains
* Prompt Engineering

---

## 📂 Project Structure

```text
youtube-rag-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/youtube-rag-chatbot.git

cd youtube-rag-chatbot
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Usage

Update the YouTube video ID inside `app.py`:

```python
video_id = "7nGN11DW-b0"
```

Run the application:

```bash
python app.py
```

Example questions:

```text
What is this video about?

Summarize the video in 5 bullet points.

Is alien life discussed in the video?

Who is Demis?
```

---

## 🔄 RAG Pipeline

1. Fetch YouTube transcript
2. Convert transcript to text
3. Split transcript into chunks
4. Generate embeddings
5. Store vectors in FAISS
6. Retrieve relevant chunks
7. Send context + question to LLM
8. Generate grounded response

```text
YouTube Video
      ↓
Transcript
      ↓
Text Splitter
      ↓
Embeddings
      ↓
FAISS Vector Store
      ↓
Retriever
      ↓
LLM
      ↓
Answer
```

---

## 📸 Sample Output

Question:

```text
Is alien life discussed in the video?
```

Answer:

```text
Based on the retrieved context, the speaker discusses the possibility of alien civilizations and explores scientific arguments related to extraterrestrial life.
```

---

## 🎯 Learning Outcomes

This project helped me understand:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* Text Splitting Strategies
* LangChain Runnables
* Prompt Engineering
* Semantic Search

---

## 🔮 Future Improvements

* Support multiple YouTube videos
* Streamlit user interface
* Persistent vector storage
* Conversation memory
* Hybrid search
* Re-ranking
* Agentic workflows

---

## 👨‍💻 Author

**Nikhil Reddy**

Linux Administrator | Learning Generative AI | Building AI Applications with LangChain and OpenAI

Feel free to connect and share feedback!
