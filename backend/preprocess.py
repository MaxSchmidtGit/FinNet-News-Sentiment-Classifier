import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def clean_text(text: str) -> str:
    """
    Cleans and lemmatizes the input text using spaCy.
    Removes stopwords and punctuation.
    """
    doc = nlp(text.lower())
    cleaned = " ".join(
        token.lemma_ for token in doc if not token.is_stop and not token.is_punct
    )
    return cleaned
