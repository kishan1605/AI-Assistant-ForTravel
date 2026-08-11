from fastapi import FastAPI, File, UploadFile
from contextlib import asynccontextmanager
from pydantic import BaseModel
from src.ingestion import ingest_file
from src.vectorstore import init_qdrant

@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize resoure 
    print("initialzing qdrant DB...")
    init_qdrant()
    print("Successfully initialzed qdrant DB...")
    yield

app = FastAPI(lifespan=lifespan)

class GetQuestion(BaseModel):
    qsn: str

@app.post('/question')
async def get_question(req: GetQuestion):
    return {"question": req.qsn}

@app.post('/upload')
async def fileupload(file: UploadFile = None):
    if file == None:
        return {"message": "Please upload a file"}

    if not file.filename.endswith(".pdf"):
        return {"message": "Please upload a pdf file"}

    try:
        data = await ingest_file(file)
        return {"message": data}
    except Exception as e:
        return {"message": "error is "+ f'{str(e)}'}
