import os
import googleapiclient.discovery
from textblob import TextBlob
import matplotlib.pyplot as plt
import sys

def get_youtube_comments(video_id, api_key):
    try:
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        
        api_service_name = "youtube"
        api_version = "v3"
        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100
        )
        response = request.execute()
        
        comments = []
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
            comments.append(comment)
        
        return comments
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def analyze_sentiment(comments):
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}

    for comment in comments:
        try:
            analysis = TextBlob(comment)
            if analysis.sentiment.polarity > 0:
                sentiments['positive'] += 1
            elif analysis.sentiment.polarity == 0:
                sentiments['neutral'] += 1
            else:
                sentiments['negative'] += 1
        except Exception as e:
            print(f"An error occurred during sentiment analysis: {e}")
    
    return sentiments

def plot_sentiments(sentiments):
    labels = sentiments.keys()
    sizes = sentiments.values()
    colors = ['green', 'blue', 'red']
    explode = (0.1, 0, 0)  # explode the 1st slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.title('Sentiment Analysis of YouTube Comments')
    plt.show()

if __name__ == "__main__":
    print("Welcome to the YouTube Comments Sentiment Analyzer!")
    
    api_key = input("Please enter your YouTube Data API key: ")
    video_id = input("Please enter the YouTube video ID: ")
    
    print("Fetching comments...")
    comments = get_youtube_comments(video_id, api_key)
    if not comments:
        print("No comments found or an error occurred.")
        sys.exit(1)
    
    print("Analyzing sentiments...")
    sentiments = analyze_sentiment(comments)
    
    print("Plotting sentiments...")
    plot_sentiments(sentiments)
