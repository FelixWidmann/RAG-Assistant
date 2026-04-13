import chromadb
from chromadb.config import Settings
from Backend.Shared.config import CHROMADB_PORT, CHROMADB_HOST

chroma_client = chromadb.HttpClient(host=CHROMADB_HOST, port=CHROMADB_PORT, settings=Settings(allow_reset=True, anonymized_telemetry=False))
