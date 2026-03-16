from Backend.Shared.ingestion_resources import CHUNKER
from Backend.Shared.ingestion_resources import TOKENIZER

def chunking(document, key):

    chunk_iter = CHUNKER.chunk(
        dl_doc=document, 
        max_tokens=512,
        overlap=50,
        include_metadata=True
        )
    
    contextualized_chunks = []

    for i, chunk in enumerate(chunk_iter):
        
        enriched_text = CHUNKER.contextualize(chunk=chunk)
        prefixed_text = "passage: " + enriched_text #prefix chunk for retrieval quality

        chunk_id = f"{key}_{i}"
        contextualized_chunks.append({
                "id": chunk_id,
                "text": prefixed_text,
                "metadata" : {
                    "page": getattr(chunk.meta, "page_no", 00),
                    "section": getattr(chunk.meta, "section_title", ""),

                }
            })
        
    return contextualized_chunks