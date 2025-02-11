import praw
from textblob import TextBlob
from config import config

# Conexão com o Reddit
reddit = praw.Reddit(
    client_id=config["reddit_client_id"],
    client_secret=config["reddit_client_secret"],
    user_agent=config["reddit_user_agent"]
)

def get_sentiment(termo):
    comentarios = reddit.subreddit("cryptocurrency").search(termo, limit=50)
    polaridade_total, total = 0, 0
    for comentario in comentarios:
        if hasattr(comentario, "selftext"):
            analise = TextBlob(comentario.selftext)
            polaridade_total += analise.sentiment.polarity
            total += 1
    return round(polaridade_total / total, 2) if total > 0 else 0
