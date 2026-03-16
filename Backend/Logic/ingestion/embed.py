from Backend.Shared.ingestion_resources import MODEL

def embed(chunks: list):

    chunk_texts = [c["text"] for c in chunks]
    
    embeddings = MODEL.encode(
        chunk_texts,
        batch_size=64,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    #store embedding with metadata and chunk.
    for chunk, emb in zip(chunks, embeddings):
        chunk["embedding"] = emb

    return chunks #return list of objects containing Chunk, metadata and embedding.