

# **Mini XtractEdge – Intelligent Document Processing (IDP)**

*A lightweight, open-source clone of EdgeVerve’s XtractEdge — built for OCR, document classification, and key-value extraction.*

---

## 🚀 Overview

Mini XtractEdge is an end-to-end **Intelligent Document Processing (IDP)** system that takes PDFs/images and extracts:

✔ OCR Text
✔ Document Type (Invoice / Resume / ID card / etc.)
✔ Key Fields (Name, Date, Total, Address…)
✔ Exports in JSON + Excel

Built using: **FastAPI, Tesseract OCR, spaCy, scikit-learn, Vanilla JS frontend**

---

## ✨ Features

* **OCR Engine** → Tesseract + pdf2image
* **ML Classifier** → Naive Bayes / Linear SVC
* **NLP Key Extraction** → spaCy patterns
* **Exports** → JSON + Excel
* **Interactive API Docs** → Swagger UI
* **Simple Frontend UI**

---

## 📁 Project Structure

```
mini-xtractedge/
│── backend/
│   └── app/
│       ├── main.py
│       ├── ocr_utils.py
│       ├── classifier.py
│       ├── extractor.py
│       └── export_utils.py
│   └── requirements.txt
│
│── training/
│   └── train_classifier.py
│
│── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
└── sample_data/
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repo

```bash
git clone https://github.com/Annrhayan23/mini-xtractedge
cd mini-xtractedge
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r backend/requirements.txt
pip install scikit-learn
```

### 4️⃣ Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 5️⃣ Install Tesseract OCR

Download (Windows):
[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

Add this to PATH:

```
C:\Program Files\Tesseract-OCR\
```

---

## ▶️ Running the App

### **Start Backend**

```bash
uvicorn backend.app.main:app --reload --port 8000
```

API Docs:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

### **Start Frontend**

```bash
cd frontend
python -m http.server 8080
```

UI:
👉 [http://localhost:8080](http://localhost:8080)

---

## 🧠 Train Your Own Classifier

Add folders inside `sample_data`:

```
sample_data/
   invoice/
   resume/
   idcard/
   others/
```

Then run:

```bash
python training/train_classifier.py
```

Generates:

```
backend/app/models/classifier.joblib
backend/app/models/vectorizer.joblib
```

---

## 📤 Extraction Output Example

```json
{
  "doc_type": "invoice",
  "confidence": 0.94,
  "extracted_fields": {
    "invoice_no": "INV-2024-0012",
    "date": "12-04-2024",
    "total": "₹18,500"
  },
  "exports": {
    "json": "exports/output_123.json",
    "excel": "exports/output_123.xlsx"
  }
}
```

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **OCR:** Tesseract
* **NLP:** spaCy
* **ML:** scikit-learn
* **Frontend:** HTML + JS

---

## ⭐ Why this Project?

This project shows recruiters that you know:

✔ AI (OCR + NLP + ML)
✔ End-to-end product building
✔ API development
✔ Frontend integration
✔ Data engineering & pipelines

Perfect for: **AI Engineer / ML Engineer / RPA / Automation / IDP roles**.

---

## 🧑‍💻 Author

**Ann Rhayan**
AI/ML Developer • Automation Enthusiast
🚀 *Building cool things with OCR + NLP + ML*

---
