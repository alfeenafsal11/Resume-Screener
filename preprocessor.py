import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import string

# Ensure necessary resources are available
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    fdist = FreqDist(filtered_tokens)
    keywords = fdist.most_common(40)
    keylist = [i[0] for i in keywords]

    # Append domain-specific keywords
    tech_keywords = ['python', 'java', 'c++', 'sql', 'machine', 'learning', 'django', 'react', 'git', 'docker', 'aws']
    keylist.extend(tech_keywords)
    return keylist
