import fitz
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def resume_check(resume_file, keywords, threshold):
    # Handle both file paths and file-like objects
    if hasattr(resume_file, 'read'):
        doc = fitz.open(stream=resume_file.read(), filetype="pdf")
    else:
        doc = fitz.open(resume_file)

    res_text = ""
    for page in doc:
        res_text += page.get_text()
    doc.close()

    tokens = word_tokenize(res_text.lower())
    filtered_tokens = [t for t in tokens if t not in stop_words and t not in string.punctuation]
    res_keywords = [t for t in filtered_tokens if t.isalpha()]

    matched = [k for k in keywords if k in res_keywords]
    score = len(matched) / len(keywords)
    result = score >= (threshold / 100)
    return result, score
