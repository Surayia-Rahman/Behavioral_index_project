
# Linguistic fingerprinting based on:
# - LIWC-style word categories (Pennebaker et al.)
# - Social vs self-focus metrics

from collections import Counter
import numpy as np

SELF_FOCUS = {"i", "me", "my", "mine"}
SOCIAL = {"we", "us", "our", "people", "everyone"}
DOMINANCE = {"must", "should", "always", "never", "obviously"}
AGGRESSION = {"hate", "angry", "furious", "annoyed", "stupid"}

def extract_personality_features(processed_sample, sentiment_analyzer):
    text = processed_sample["clean_text"].lower()
    words = text.split()
    total = len(words) if len(words) > 0 else 1
    counts = Counter(words)

    self_focus = sum(counts[w] for w in SELF_FOCUS) / total
    social_focus = sum(counts[w] for w in SOCIAL) / total
    dominance = sum(counts[w] for w in DOMINANCE) / total
    aggression = sum(counts[w] for w in AGGRESSION) / total

    sentiment = sentiment_analyzer.polarity_scores(text)["compound"]
    emotional_intensity = abs(sentiment)

    lexical_diversity = len(set(words)) / total

    return {
        "self_focus": self_focus,
        "social_focus": social_focus,
        "dominance": dominance,
        "aggression": aggression,
        "emotional_intensity": emotional_intensity,
        "lexical_diversity": lexical_diversity
    }
