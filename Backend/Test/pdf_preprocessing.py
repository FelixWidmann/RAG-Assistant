from docling.document_converter import DocumentConverter, DocumentStream
from docling.chunking import HybridChunker
from io import BytesIO
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
from Backend.Shared.minio_client import s3_client
#from Backend.Shared.chromadb_client import CHROMADB_COLLECTION

BUCKET_NAME = "library"
KEY = "Advances_Financial_Machine_Learning_very_short.pdf"

MODEL = SentenceTransformer("intfloat/e5-base-v2")
TOKENIZER = AutoTokenizer.from_pretrained("intfloat/e5-base-v2")

CONVERTER = DocumentConverter()
CHUNKER = HybridChunker(
    tokenizer=TOKENIZER,
    merge_peers=True,  # optional, defaults to True
    )

def download_from_minio(key: str):

    response = s3_client.get_object(
        Bucket=BUCKET_NAME,
        Key=key,
    )
    file_bytes = response["Body"].read()

    return file_bytes, key

def extract_text_from_pdf(pdf_bytes: bytes, key: str):

    file = BytesIO(pdf_bytes)

    stream = DocumentStream(name = key, stream = file)

    result = CONVERTER.convert(stream)

    document = result.document if hasattr(result, "document") else result

    #markdown_output = document.export_to_markdown() #only for testing. IN productino export to markdown is not needed. 

    return document


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
        
        #assign unique chunk_id to each chunk for storing.
        chunk_id = f"{key}_{i}"

        #extract page number and headings of the chunk
        pages = set()
        headings = []
        headings.extend(chunk.meta.headings)

        for item in chunk.meta.doc_items:
            for prov in getattr(item, "prov", []):
                    pages.add(prov.page_no)


        contextualized_chunks.append({
                "id": chunk_id,
                "text": prefixed_text,
                "metadata": {
                    "page": pages,
                    "headings": headings,
                }
            })
        
    return contextualized_chunks


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


# def store_embeddings(docs):

#     CHROMADB_COLLECTION.add(
#     ids=[d["id"] for d in docs],
#     documents=[d["text"] for d in docs],
#     metadatas=[d["metadata"] for d in docs],
#     embeddings=[d["embedding"] for d in docs]
#     )
    
#     results = CHROMADB_COLLECTION.get(
#     # no filter means get everything
#     ids=None,
#     where=None,
#     limit=None  # None returns all
# )

#     return results

def ingest_document(key: str):
    
    # download PDF
    pdf_bytes, _ = download_from_minio(key)

    # extract text
    document = extract_text_from_pdf(pdf_bytes, KEY)

    #chunk text
    contexted_chunks = chunking(document, key)

    #embed text
    embed_chunks = embed(contexted_chunks)

    #results = store_embeddings(embed_chunks)

    return embed_chunks



def main():
    
    result = ingest_document(KEY)

    # print first chunk
    #print(str(len(result)))
    #print(result)

if __name__ == "__main__":
    main()
