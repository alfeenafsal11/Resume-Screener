import fitz

def extract_text(file):
    if hasattr(file, 'read'):
        doc = fitz.open(stream=file.read(), filetype="pdf")
    else:
        doc = fitz.open(file)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text
