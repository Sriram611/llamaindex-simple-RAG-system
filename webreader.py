from llama_index.core import VectorStoreIndex, Settings
from llama_index.readers.web import SimpleWebPageReader
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from dotenv import load_dotenv

load_dotenv()

Settings.llm = GoogleGenAI(model="gemini-2.5-flash")

Settings.embed_model = GoogleGenAIEmbedding(
    model_name="models/gemini-embedding-001"
)

documents = SimpleWebPageReader(html_to_text=True).load_data(
    urls=["https://en.wikipedia.org/wiki/Generative_artificial_intelligence"]
)

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query("What is transformer?")

print(response)