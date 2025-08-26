from data_collection import get_comments
from preprocessing import clean_comment_parallel
from sentiment_analysis import analyze_sentiment_parallel
from theme_detection import detect_themes
from visualization import plot_combined_view

def main():
    api_key = 'AIzaSyBTRz5PFYvQ1btVtYy2IJoI5iPlhUmR0AA'
    video_id = input("Enter the YouTube video ID: ")

    # Collect comments
    comments = get_comments(video_id, api_key)[:200]

    # Preprocess and analyze in parallel
    cleaned_comments = clean_comment_parallel(comments)
    sentiments = analyze_sentiment_parallel(cleaned_comments)
    themes = detect_themes(cleaned_comments)

    # Visualize combined results
    plot_combined_view(sentiments, themes)

if __name__ == "__main__":
    main()
#example-eophOsbkBv0