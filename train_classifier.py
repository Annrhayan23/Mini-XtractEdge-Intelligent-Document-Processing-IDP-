import os, joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def load_dataset(d):
    X, y = [], []
    for label in os.listdir(d):
        path = os.path.join(d, label)
        for f in os.listdir(path):
            with open(os.path.join(path, f), "r", errors="ignore") as fp:
                X.append(fp.read())
                y.append(label)
    return X, y

# <-- FIXED PATH
X, y = load_dataset("training/sample_data")

vec = TfidfVectorizer()
Xv = vec.fit_transform(X)

clf = LogisticRegression(max_iter=2000).fit(Xv, y)

os.makedirs("../backend/app/models", exist_ok=True)
joblib.dump(clf, "../backend/app/models/classifier.joblib")
joblib.dump(vec, "../backend/app/models/vectorizer.joblib")

print("Model trained!")
