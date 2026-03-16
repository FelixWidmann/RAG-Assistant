from Backend.Logic.ingestion.pdf_download import download_from_minio
from Backend.Logic.ingestion.pdf_extractor import extract_text_from_pdf
from Backend.Logic.ingestion.chunker import chunking
from Backend.Logic.ingestion.embed import embed
from Backend.Logic.ingestion.store_vectordb import store_embeddings


def orchestrate_ingestion(key: str):
    
    #download requested file from minio
    pdf_bytes = download_from_minio(key)

    #extract pdf
    document = extract_text_from_pdf(pdf_bytes, key)

    #chunk text
    contexted_chunks = chunking(document, key)

    #embed text
    embed_chunks = embed(contexted_chunks)

    #store embeddings
    success, message = store_embeddings(embed_chunks)

    return success, message
