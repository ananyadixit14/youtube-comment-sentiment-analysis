import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_combined_view(sentiments, themes):
    # Filter out None values from themes
    filtered_themes = [theme for theme in themes if theme is not None]
    
    # Check if there are valid themes to display
    if not filtered_themes:
        print("No valid themes detected. Skipping word cloud visualization.")
        filtered_themes = ["No themes detected"]

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Sentiment Distribution
    axes[0].hist(sentiments, bins=3, color='blue', edgecolor='black', rwidth=0.8)
    axes[0].set_title('Sentiment Distribution')
    axes[0].set_xlabel('Sentiment')
    axes[0].set_ylabel('Frequency')

    # Word Cloud for Themes
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(filtered_themes))
    axes[1].imshow(wordcloud, interpolation='bilinear')
    axes[1].axis('off')
    axes[1].set_title('Word Cloud of Themes')

    plt.tight_layout()
    plt.show()
