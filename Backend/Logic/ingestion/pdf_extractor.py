from docling.document_converter import DocumentStream
from io import BytesIO
from Backend.Shared.ingestion_resources import CONVERTER


def extract_text_from_pdf(pdf_bytes: bytes, key: str):

    file = BytesIO(pdf_bytes)

    stream = DocumentStream(name = key, stream = file)

    result = CONVERTER.convert(stream)

    document = result.document if hasattr(result, "document") else result

    #markdown_output = document.export_to_markdown() #only for testing. IN productino export to markdown is not needed. 

    return document
