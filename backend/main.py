from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from models import create_db_and_tables, Job, SessionLocal
from utils import process_image
import shutil, os

app = FastAPI()

@app.on_event("startup")
def startup():
    create_db_and_tables()

@app.post("/remove-background/")
async def remove_background(file: UploadFile = File(...)):
    db = SessionLocal()
    upload_path = f\"uploads/{file.filename}\"
    processed_path = f\"processed/processed_{file.filename}\"

    with open(upload_path, \"wb\") as buffer:
        shutil.copyfileobj(file.file, buffer)

    process_image(upload_path, processed_path)

    job = Job(original_file=upload_path, processed_file=processed_path, status=\"completed\")
    db.add(job)
    db.commit()

    return {\"download_url\": f\"/download/{job.id}\"}

@app.get(\"/download/{job_id}\")
def download_file(job_id: int):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()
    return FileResponse(path=job.processed_file, filename=os.path.basename(job.processed_file))
