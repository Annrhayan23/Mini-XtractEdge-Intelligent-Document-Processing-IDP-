import json, pandas as pd, os

def export_json(data, filename):
    os.makedirs("exports", exist_ok=True)
    path = f"exports/{filename}"
    with open(path, "w") as f: json.dump(data, f, indent=4)
    return path

def export_excel(data, filename):
    os.makedirs("exports", exist_ok=True)
    path = f"exports/{filename}"
    pd.DataFrame([data]).to_excel(path, index=False)
    return path