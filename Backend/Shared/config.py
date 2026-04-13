import os

MINIO_HOST = os.getenv("MINIO_HOST")
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY",)
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY",)
MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")

# Chunker details
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
OVERLAP = int(os.getenv("OVERLAP"))
INCLUDE_METADATA = os.getenv("INCLUDE_METADATA")

# Embedding Model + Tokenizer
MODEL_NAME = os.getenv("MODEL_NAME", "intfloat/e5-base-v2") #intfloat/multilingual-e5-base

# ChromaDB
CHROMADB_HOST = os.getenv("CHROMADB_HOST")
CHROMADB_DIRECTORY = os.getenv("CHROMADB_DIRECTORY")
CHROMADB_PORT = int(os.getenv("CHROMADB_PORT"))

# Language Model
LANGUAGE_MODEL = os.getenv("LANGUAGE_MODEL", "llama3.2")
OLLAMA_NUM_BATCH = int(os.getenv("OLLAMA_NUM_BATCH"))
OLLAMA_CONTEXT_LENGTH = int(os.getenv("OLLAMA_CONTEXT_LENGTH"))
OLLAMA_HOST = os.getenv("OLLAMA_HOST")
LANGUAGE_MODEL_ENDPOINT = os.getenv( "LANGUAGE_MODEL_ENDPOINT")


# # MinIO connection details
# MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://minio:9000")
# MINIO_HOST = os.getenv("MINIO_HOST", "minio")
# MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY",)
# MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY",)
# BUCKET_NAME = os.getenv("BUCKET_NAME", "library")

# # Chunker details
# MAX_TOKENS = int(os.getenv("MAX_TOKENS", 512))
# OVERLAP = int(os.getenv("OVERLAP", 50))
# INCLUDE_METADATA = os.getenv("INCLUDE_METADATA", "True") == "True"

# # Embedding Model + Tokenizer
# MODEL_NAME = os.getenv("MODEL_NAME", "intfloat/e5-base-v2") #intfloat/multilingual-e5-base

# # ChromaDB
# CHROMADB_HOST = os.getenv("CHROMADB_HOST", "chromadb")
# CHROMADB_COLLECTION_NAME = os.getenv("CHROMADB_COLLECTION_NAME", "embedded_library")
# CHROMADB_DIRECTORY = os.getenv("CHROMADB_DIRECTORY", "./chromadb")
# CHROMADB_PORT = int(os.getenv("CHROMADB_PORT", 8000))

# # Language Model
# LANGUAGE_MODEL = os.getenv("LANGUAGE_MODEL", "llama3.2")
# OLLAMA_HOST = os.getenv("OLLAMA_HOST", "ollama")
# LANGUAGE_MODEL_ENDPOINT = os.getenv(
#     "LANGUAGE_MODEL_ENDPOINT",
#     "http://ollama:11434/api/generate"
# )