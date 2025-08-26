from gensim import corpora
from gensim.models import LdaModel
from preprocessing import clean_comment

# Expanded theme categories with example keywords
CATEGORIES = {
    "comedy": ["funny", "joke", "laugh", "humor", "comedy", "parody", "satire", "skit"],
    "action": ["fight", "battle", "chase", "hero", "action", "adventure", "war", "combat"],
    "political": ["government", "politics", "policy", "law", "election", "candidate", "vote", "debate"],
    "social": ["community", "society", "help", "support", "social", "justice", "rights", "awareness"],
    "drama": ["love", "family", "relationship", "life", "emotions", "tragedy", "conflict"],
    "technology": ["tech", "gadget", "software", "review", "unboxing", "innovation", "device", "app", "programming"],
    "science": ["experiment", "discovery", "biology", "physics", "chemistry", "research", "study", "science", "theory"],
    "education": ["learn", "lesson", "tutorial", "course", "teacher", "class", "knowledge", "study", "school","coding","code"],
    "music": ["song", "album", "track", "music", "band", "instrument", "concert", "melody", "lyrics"],
    "sports": ["game", "match", "sport", "team", "score", "player", "tournament", "goal", "athlete"],
    "news": ["breaking", "headline", "news", "report", "current", "update", "journalism", "coverage"],
    "health": ["wellness", "fitness", "exercise", "diet", "mental", "health", "nutrition", "therapy", "doctor"],
    "lifestyle": ["travel", "food", "fashion", "beauty", "style", "vlog", "day", "life", "experience"],
    "motivational": ["inspiration", "motivation", "success", "goal", "achievement", "self", "growth", "mindset"],
    "horror": ["scary", "ghost", "paranormal", "horror", "creepy", "mystery", "fear", "thriller"],
    "crime": ["crime", "murder", "detective", "case", "investigation", "police", "law", "suspect"],
    "finance": ["money", "investment", "stock", "market", "finance", "economy", "banking", "crypto", "trade"],
    "environment": ["nature", "planet", "climate", "earth", "environment", "pollution", "conservation", "wildlife"],
    "gaming": ["game", "level", "play", "gamer", "console", "tournament", "live", "score", "stream"],
    "religion devotional": ["faith", "spiritual", "belief", "religion", "church", "god", "worship", "prayer", "bible","jai shree ram","ram","hanuman","bajrangbali"],
    "documentary": ["real", "documentary", "history", "facts", "profile", "analysis", "footage", "background"],
    "DIY": ["tutorial", "guide", "DIY", "craft", "project", "how-to", "homemade", "repair", "create"],
    "kids": ["children", "kid", "cartoon", "toy", "fun", "learn", "play", "family-friendly", "activity"],
}

def categorize_theme(keywords):
    category_scores = {category: 0 for category in CATEGORIES}
    for keyword in keywords:
        for category, cat_keywords in CATEGORIES.items():
            if keyword in cat_keywords:
                category_scores[category] += 1
    best_category = max(category_scores, key=category_scores.get)
    return best_category if category_scores[best_category] > 0 else None

def detect_themes(comments, num_topics=3):
    processed_comments = [clean_comment(comment).split() for comment in comments]
    dictionary = corpora.Dictionary(processed_comments)
    corpus = [dictionary.doc2bow(text) for text in processed_comments]
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=5)  # Reduced passes
    themes = []

    for idx, topic in lda_model.show_topics(formatted=False):
        topic_keywords = [word for word, _ in topic]
        themes.append(categorize_theme(topic_keywords))
    
    return themes