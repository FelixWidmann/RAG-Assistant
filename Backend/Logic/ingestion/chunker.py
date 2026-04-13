from Backend.Shared.ingestion_resources import CHUNKER, TOKENIZER 
from Backend.Shared.config import MAX_TOKENS, OVERLAP

def chunking(document, key):

    chunk_iter = CHUNKER.chunk(
        dl_doc=document, 
        max_tokens=MAX_TOKENS,
        overlap=OVERLAP,
        include_metadata=True
        )
    
    contextualized_chunks = []

    for i, chunk in enumerate(chunk_iter):
        
        enriched_text = CHUNKER.contextualize(chunk=chunk)
        prefixed_text = "passage: " + enriched_text #prefix chunk for retrieval quality
        
        #assign unique chunk_id to each chunk for storing.
        chunk_id = f"{key}_{i}"

        #extract page number and headings of the chunk
        pages = set()
        headings = []

        reference_names = {"references", "References", "Literature", "literature", "Keywords"}

        #check if heading is None, return empty list or heading.
        if chunk.meta.headings != None:
             headings.extend(chunk.meta.headings)
             
             #If Section heading is references --> skip
             if chunk.meta.headings[0] in reference_names: 
                continue
        else:
             headings.extend(["No heading"])


        for item in chunk.meta.doc_items:
            for prov in getattr(item, "prov", []):
                    pages.add(prov.page_no)
        
        #List with unique page numbers per chunk - [6,6,6,7] --> [6,7]
        unique_pages = list(pages)

        contextualized_chunks.append({
                "id": chunk_id,
                "text": prefixed_text,
                "metadata": {
                    "page": unique_pages,
                    "headings": headings,
                    "document": key,
                }
            })
        
    return contextualized_chunks