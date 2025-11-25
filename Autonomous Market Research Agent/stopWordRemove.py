import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def remove_stopwords(query: str) -> str:
    doc = nlp(query)
    filtered_tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(filtered_tokens)

# Example
# query = "What is the top AI tools for SEO in 2025?"
# clean_query = remove_stopwords(query)
# print("Original:", query)
# print("Without Stopwords:", clean_query)