from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from youtube_transcript_api.proxies import WebshareProxyConfig

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnableLambda,
    RunnablePassthrough,
)
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# -----------------------------
# Step 1: Get YouTube Transcript
# -----------------------------

video_id = "7nGN11DW-b0"

try:
    ytt_api = YouTubeTranscriptApi(
        proxy_config=WebshareProxyConfig(
            proxy_username="twepydjq",
            proxy_password="jg0a7k6lqtt7",
        )
    )

    transcript_list = ytt_api.fetch(video_id, languages=["en"])

    transcript = " ".join(
        chunk.text for chunk in transcript_list
    )

except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")
    exit()

# -----------------------------
# Step 2: Split Transcript
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

documents = text_splitter.create_documents(
    [transcript],
    metadatas=[{"video_id": video_id}]
)

# -----------------------------
# Step 3: Create Vector Store
# -----------------------------

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = FAISS.from_documents(
    documents,
    embedding_model
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# -----------------------------
# Step 4: LLM + Prompt
# -----------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Answer the question only using the provided context.

If the answer is not present in the context,
respond with: "I don't know."

Context:
{context}

Question:
{question}
""",
    input_variables=["context", "question"]
)

# -----------------------------
# Step 5: Build RAG Chain
# -----------------------------

def format_docs(docs):
    return "\n\n".join(
        doc.page_content for doc in docs
    )

rag_chain = (
    RunnableParallel(
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
    )
    | prompt
    | llm
    | StrOutputParser()
)

# -----------------------------
# Step 6: Ask Questions
# -----------------------------

question = (
    "Is alien life discussed in the video? "
    "If yes, what was discussed?"
)

response = rag_chain.invoke(question)

print("\nAnswer:\n")
print(response)

summary = rag_chain.invoke(
    "Summarize the video in 5 bullet points."
)

print("\nSummary:\n")
print(summary)