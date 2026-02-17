from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression

model = LogisticRegression('all-MiniLM-L6-v2')
def train_classifier(text, labels):
    embedded = model.encode(text)
    clf = LogisticRegression(max_iter=1000)
    clf.fit(embedded, labels)
    return clf

def predict_category(text, clf):
    emd = model.encode([text])
    return clf.predict(emd)[0]

def predict_priority(text):
    urgent_words =  ["urgent", "charged","failed","error","crash"]
    if any(word in text.lower() for word in urgent_words):
        return "High"
    return 'Low'