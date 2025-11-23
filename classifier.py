import joblib, os

def load_model():
    mp = "backend/app/models/classifier.joblib"
    vp = "backend/app/models/vectorizer.joblib"
    if not os.path.exists(mp): return None, None
    return joblib.load(mp), joblib.load(vp)

def predict_doc_type(text, model, vectorizer):
    if model is None: return "unknown", 0.0
    vec = vectorizer.transform([text])
    proba = model.predict_proba(vec)[0]
    return model.classes_[proba.argmax()], float(max(proba))