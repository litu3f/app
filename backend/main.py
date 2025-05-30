from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import shutil, os
from models import create_db_and_tables, Job, get_db
from utils import process_image

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
def startup():
    create_db_and_tables()

@app.post("/remove-background/")
def remove_background(file: UploadFile = File(...), db: Session = Depends(get_db)):
    upload_path = f"uploads/{file.filename}"
    processed_path = f"processed/processed_{file.filename}"
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    process_image(upload_path, processed_path)
    job = Job(original_file=upload_path, processed_file=processed_path, status="completed")
    db.add(job)
    db.commit()
    return {"message": "Background removed", "download_url": f"/download/{job.id}"}

@app.get("/download/{job_id}")
def download(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    return FileResponse(path=job.processed_file, filename=os.path.basename(job.processed_file))
