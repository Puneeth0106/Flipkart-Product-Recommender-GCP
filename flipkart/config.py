import os
from dotenv import load_dotenv
load_dotenv()

class Config:   
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    ASTRA_DB_API_ENDPOINT= os.getenv("ASTRA_DB_API_ENDPOINT")
    ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")
    RAG_MODEL = "openai/gpt-oss-120b"
    EMBEDDING_MODEL = "Jarbas/m2v-256-bge-base-en-v1.5"