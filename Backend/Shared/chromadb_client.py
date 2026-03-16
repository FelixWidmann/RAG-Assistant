import chromadb
from Backend.Shared.config import CHROMADB_COLLECTION_NAME, CHROMADB_DIRECTORY, CHROMADB_PORT

chroma_client = chromadb.HttpClient(host='localhost', port=CHROMADB_PORT)

CHROMADB_COLLECTION = chroma_client.get_or_create_collection(name=CHROMADB_COLLECTION_NAME,  embedding_function = None)
