from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from Backend.Logic.projects.collection_management import get_collection_list, create_collection, delete_collection

class CollectionInfo(BaseModel):
    name: str

project_router = APIRouter()

@project_router.get("/collections")
def fetch_collection_list():

    try:
        
        collection_list = get_collection_list()

        return collection_list
    
    except Exception as e: 
    
        raise HTTPException(status_code=500, detail = str(e))



@project_router.post("/addcollection")
def create_new_collection(request: CollectionInfo):

    name = request.name

    try:
        
        response = create_collection(name)

        return response
    
    except Exception as e:

        raise HTTPException(status_code=500, detail= str(e))

@project_router.post("/deletecollection")
def create_new_collection(request: CollectionInfo):

    name = request.name

    try:
        
        delete_collection(name)
    
    except Exception as e: 

        raise HTTPException(status_code=500, detail= str(e))
