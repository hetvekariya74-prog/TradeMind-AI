"""TradeMind AI — Sentiment Analysis"""
import pandas as pd
from typing import List


def analyze(text: str) -> dict:
    try:
        from textblob import TextBlob
        blob = TextBlob(text)
        p    = blob.sentiment.polarity
        s    = blob.sentiment.subjectivity
    except Exception:
        p, s = 0.0, 0.0

    if p > 0.1:   label, emoji = "Positive", "😀"
    elif p < -0.1: label, emoji = "Negative", "😞"
    else:          label, emoji = "Neutral",  "😐"

    return {"polarity": round(p,4), "subjectivity": round(s,4),
            "label": label, "emoji": emoji, "confidence": int(abs(p)*100)}


MOCK_HEADLINES = [
    "Markets rally as tech stocks surge on strong earnings results.",
    "Crypto assets recover amid renewed institutional buying interest.",
    "Federal Reserve signals potential pause in rate hike cycle.",
    "Recession fears persist as PMI data disappoints economists.",
    "Oil prices fall sharply on demand concerns from China slowdown.",
]


def analyze_bulk(texts: List[str]) -> pd.DataFrame:
    return pd.DataFrame([{**analyze(t), "text": t} for t in texts])[
        ["text","label","polarity","subjectivity","confidence","emoji"]
    ]


def news_sentiment(query: str) -> dict:
    headlines = MOCK_HEADLINES
    results   = analyze_bulk(headlines)
    avg       = results["polarity"].mean()
    if avg > 0.05:   label, emoji = "Bullish", "📈"
    elif avg < -0.05: label, emoji = "Bearish", "📉"
    else:             label, emoji = "Neutral", "➡️"
    return {"polarity": round(avg,4), "label": label, "emoji": emoji,
            "n": len(headlines), "df": results}
