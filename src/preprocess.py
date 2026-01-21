import re

# This function basically cleans the text making sure it suites the what the models works with 
def preprocess(text):
    text = re.sub(r"^[a-zA-Z\s]", "", text)
    text = text.lower().strip()
    return text
