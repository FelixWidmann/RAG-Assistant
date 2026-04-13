from Backend.Logic.retrieval.embed_query import EmbeddedQuery
from chromadb import Collection

def retrieve(embedded_query: EmbeddedQuery, collection: Collection):

    try:

        results = collection.query(
        query_embeddings=[embedded_query.embedding],
        n_results=4)

        return results
    
    except Exception as e:
        
        raise RuntimeError(f"Failed to query Embeddings") from e


#     {
#     "ids": [["doc1", "doc5", "doc2"]],
#     "documents": [["Text of doc1", "Text of doc5", "Text of doc2"]],
#     "metadatas": [[{...}, {...}, {...}]],
#     "distances": [[0.12, 0.18, 0.23]],
#     "embeddings": None
# }
