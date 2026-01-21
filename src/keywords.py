import spacy

nlp = spacy.load("en_core_web_en")

def extract_keywords(text):
    doc = nlp(text)
    return [chunk.text for chunk in doc.noun_chunks]
