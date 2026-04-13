from Backend.Shared.ingestion_resources import MODEL
from pydantic import BaseModel

class EmbeddedQuery(BaseModel):
    query: str
    embedding: list[float]

def embed_query(query: str):
    
    embedding = MODEL.encode(
        query,
        normalize_embeddings=True,
    )

    embedded_query = EmbeddedQuery(
        query = query, 
        embedding = embedding.tolist() #ChromaDb expects embedding as list of floats.
        )

    return embedded_query