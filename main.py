from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

from .ocr_utils import extract_text
from .classifier import load_model, predict_doc_type
from .extractor import extract_key_fields
from .export_utils import export_json, export_excel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL, VECTORIZER = load_model()

@app.post("/process")
async def process_document(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text(file_path)
    doc_type, confidence = predict_doc_type(text, MODEL, VECTORIZER)
    fields = extract_key_fields(text, doc_type)

    json_path = export_json(fields, file.filename + ".json")
    excel_path = export_excel(fields, file.filename + ".xlsx")

    return {
        "doc_type": doc_type,
        "confidence": confidence,
        "extracted_fields": fields,
        "json_export": json_path,
        "excel_export": excel_path,
    }

@app.get("/")
def home():
    return {"msg": "Mini XtractEdge API running"}