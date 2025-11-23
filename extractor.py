import re, spacy
nlp = spacy.load("en_core_web_sm")

def find(pattern, text):
    m = re.search(pattern, text, re.I)
    return m.group(1) if m else None

def extract_key_fields(text, doc_type):
    d = {}
    if doc_type == "invoice":
        d["invoice_number"] = find(r"Invoice\s*#?\s*([\w-]+)", text)
        d["amount"] = find(r"Total[:\s]*\$?(\d+\.\d{2})", text)
        d["date"] = find(r"(\d{2}/\d{2}/\d{4})", text)
    elif doc_type == "resume":
        doc = nlp(text)
        persons = [e.text for e in doc.ents if e.label_=="PERSON"]
        d["name"] = persons[0] if persons else None
        d["email"] = find(r"\S+@\S+", text)
        d["phone"] = find(r"\+?\d[\d\- ]{7,14}", text)
    elif doc_type == "idcard":
        d["id_number"] = find(r"\b[A-Z0-9]{6,12}\b", text)
        d["dob"] = find(r"\d{2}/\d{2}/\d{4}", text)
    return d