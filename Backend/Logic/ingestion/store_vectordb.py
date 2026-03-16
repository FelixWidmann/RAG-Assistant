from Backend.Shared.chromadb_client import CHROMADB_COLLECTION
from pydantic import BaseModel

class EmbeddingChunk(BaseModel):
    id: str
    text: str
    metadata: dict
    embedding: list[float]

def store_embeddings(docs: list[EmbeddingChunk]):

    try:
        CHROMADB_COLLECTION.add(
            ids=[d["id"] for d in docs],
            documents=[d["text"] for d in docs],
            metadatas=[d["metadata"] for d in docs],
            embeddings=[d["embedding"] for d in docs]
        )

        return True, "Embeddings stored successfully."

    except Exception as e:
        # Catch any error and return False
        return False, f"Failed to store embeddings: {e}"

    


