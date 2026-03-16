# MinIO connection details
MINIO_ENDPOINT = "http://127.0.0.1:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
BUCKET_NAME = "library"

#Chunker details
MAX_TOKENS=512
OVERLAP=50
INCLUDE_METADATA=True

#Embedding Model + Tokenizer
MODEL_NAME = "intfloat/e5-base-v2"

#ChromaDb Collection
CHROMADB_COLLECTION_NAME = "embedded_library"
CHROMADB_DIRECTORY = "./chromadb"
CHROMADB_PORT = 8001