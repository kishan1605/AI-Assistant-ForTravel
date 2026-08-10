from fastapi import UploadFile
import pymupdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document #Document is a DS which provide infor about the data like source of it

async def ingest_file(file: UploadFile):
    print("Proceesing file " + f'{file.filename}')

    content = await file.read()

    docs = []
    pdf_file = pymupdf.open(stream = content, filetype = 'pdf')
    page_count = len(pdf_file)
    print(f'page count: {page_count}')

    try:
        for page_no in range(page_count):
            pdf = pdf_file[page_no]
            text = pdf.get_text()
            docs.append(Document(
                page_content = text,
                metadata = {"page" : page_no, "source": file.filename}
            ))
    finally:
        pdf_file.close()

    print("splitting...")
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 100)
    chunks = splitter.split_documents(docs)
    print(f'The chunk size is of size {len(chunks)}')

    return chunks 

    

    