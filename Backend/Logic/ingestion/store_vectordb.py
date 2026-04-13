from pydantic import BaseModel
from chromadb import Collection

class EmbeddingChunk(BaseModel):
    id: str
    text: str
    metadata: dict
    embedding: list[float]

def store_embeddings(docs: list[EmbeddingChunk], collection: Collection ):

    try:
        collection.add(
            ids=[d["id"] for d in docs],
            documents=[d["text"] for d in docs],
            metadatas=[d["metadata"] for d in docs],
            embeddings=[d["embedding"] for d in docs]
        )

        return "Embeddings stored successfully."

    except Exception as e:
        
        # Catch any error and return False
        raise RuntimeError(f"Failed to store Embeddings") from e

    


