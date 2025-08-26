import re
from concurrent.futures import ThreadPoolExecutor
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_comment(comment):
    comment = re.sub(r'http\S+', '', comment)
    comment = re.sub(r'[^A-Za-z\s]', '', comment)
    comment = comment.lower()
    words = comment.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

def clean_comment_parallel(comments):
    with ThreadPoolExecutor() as executor:
        cleaned_comments = list(executor.map(clean_comment, comments))
    return cleaned_comments
