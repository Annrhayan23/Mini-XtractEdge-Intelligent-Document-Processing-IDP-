import pytesseract
from PIL import Image
from pdf2image import convert_from_path

def extract_text(path):
    if path.endswith(".pdf"):
        pages = convert_from_path(path)
        return "".join([pytesseract.image_to_string(p) for p in pages])
    return pytesseract.image_to_string(Image.open(path))