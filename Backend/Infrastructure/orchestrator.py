from Backend.Logic.ingestion.pdf_download import download_from_minio
from Backend.Logic.ingestion.pdf_extractor import extract_text_from_pdf
from Backend.Logic.ingestion.chunker import chunking
from Backend.Logic.ingestion.embed import embed
from Backend.Logic.ingestion.store_vectordb import store_embeddings

#retrieval
from Backend.Logic.retrieval.embed_query import embed_query
from Backend.Logic.retrieval.retrieval import retrieve
from Backend.Logic.retrieval.generate_prompt import generate_prompt
from Backend.Logic.retrieval.generation import generate_answer
from Backend.Logic.projects.collection_management import get_collection

from Backend.Shared.ingestion_resources import logger


def orchestrate_ingestion(key: str, collection: str):

    try: 

        print("Downloading Document")

        #download requested file from minio
        pdf_bytes = download_from_minio(key)

        print("Creating Document", flush=True)

        #extract pdf
        document = extract_text_from_pdf(pdf_bytes, key)

        del pdf_bytes
        print("Creating Chunks", flush=True)

        #chunk text
        contexted_chunks = chunking(document, key)

        del document
        print("Computing Embeddings", flush=True)
    
        #embed text
        embed_chunks = embed(contexted_chunks)

        #get collection object
        collection_obj = get_collection(collection)

        del contexted_chunks
        print("storing Embeddings.", flush=True)

        #store embeddings
        message = store_embeddings(embed_chunks, collection_obj)

        #delete from memory after upload.
        del embed_chunks

        return message
    
    except Exception as e:

        raise RuntimeError(f"Ingestion failed for {key}: {str(e)}")



def orchestrate_query(query: str, collection: str): 

    try:

        embedded_query = embed_query(query=query) #returns Object with attribute query and embedding

        collection_obj = get_collection(collection)

        retrieved_docs = retrieve(embedded_query, collection_obj)
        
        prompt = generate_prompt(query=query, retrieved_docs= retrieved_docs)

        generated_answer = generate_answer(prompt = prompt)

        return generated_answer
    
    except Exception as e: 

        raise RuntimeError(f"Query failed: {str(e)}")