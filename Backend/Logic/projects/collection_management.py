from Backend.Shared.chromadb_client import chroma_client

def get_collection_list():

    try: 
    
        collection_list = chroma_client.list_collections() #returns list of collection objects [Collection(name=embedded_library)]

        names = [c.name for c in collection_list]

        return names
    
    except Exception as e: 

        raise RuntimeError(f"Failed to retrieve collections") from e


def create_collection(name: str):

    try:

        chroma_client.create_collection(name= name, embedding_function=None)
        
        return name
    
    except Exception as e:
        
        raise RuntimeError(f"Failed to create collection '{name}'") from e


def get_collection(name: str):

    try:

        collection_obj = chroma_client.get_collection(name=name)

        return collection_obj
    
    except Exception as e: 

        raise RuntimeError(f"Failed to get collection '{name}'") from e


def delete_collection(name: str):

    try: 

        chroma_client.delete_collection(name=name)

    except Exception as e: 

        raise RuntimeError(f"Failed to delete collection '{name}'") from e
    
