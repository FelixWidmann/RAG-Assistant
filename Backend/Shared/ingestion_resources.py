from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter

from Backend.Shared.config import MODEL_NAME


#embedding model
MODEL = SentenceTransformer(
    MODEL_NAME
    )

#tokenizer
TOKENIZER = AutoTokenizer.from_pretrained(
    MODEL_NAME
    )

#chunker
CHUNKER = HybridChunker(
    tokenizer=TOKENIZER,
    merge_peers=True,  # optional, defaults to True
    )
#Document Converter 
CONVERTER = DocumentConverter()
