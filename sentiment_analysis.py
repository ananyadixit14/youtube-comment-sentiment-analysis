from textblob import TextBlob
from concurrent.futures import ThreadPoolExecutor

def analyze_sentiment(comment):
    analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def analyze_sentiment_parallel(comments):
    with ThreadPoolExecutor() as executor:
        sentiments = list(executor.map(analyze_sentiment, comments))
    return sentiments
