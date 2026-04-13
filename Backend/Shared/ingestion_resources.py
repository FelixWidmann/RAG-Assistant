from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions

from Backend.Shared.config import MODEL_NAME

import logging


logger = logging.getLogger(__name__)


#embedding model
MODEL = SentenceTransformer(
    "/app/models/e5-base-v2", cache_folder = "/app/models/e5-base-v2", local_files_only=True
    )

#tokenizer
TOKENIZER = AutoTokenizer.from_pretrained(
    "/app/models/e5-base-v2", cache_dir =  "/app/models/e5-base-v2", local_files_only = True, max_tokens=512
    )

#chunker
CHUNKER = HybridChunker(
    tokenizer=TOKENIZER,
    max_tokens=512,
    merge_peers=True,  # optional, defaults to True
    )


#document converter
    #configure pipeline
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = False
pipeline_options.do_table_structure = True
pipeline_options.generate_picture_images = False

    #initialize Converter
CONVERTER = DocumentConverter(
    allowed_formats= [
        InputFormat.PDF
    ],
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    },
    )
