from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import shutil
import subprocess

UPLOAD_DIR = "data/uploads"

app = FastAPI()

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Document Chatbot API is running 1"}

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename.lower()

    # Basic file validation
    if not (filename.endswith(".pdf") or filename.endswith(".docx")):
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are allowed")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run ingestion after upload
    subprocess.run(["python3", "ingest.py"], check=True)

    return {
        "message": "File uploaded and ingested successfully",
        "filename": file.filename
    }
