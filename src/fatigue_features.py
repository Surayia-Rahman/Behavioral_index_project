
# Based on:
# - Cognitive Load Theory (Sweller, 1988)
# - Discourse simplification under stress (Graesser et al.)

import numpy as np
from collections import Counter

def compute_fatigue_features(processed_sample, personality_features):

    sentences = processed_sample["sentences"]
    text = processed_sample["clean_text"].lower()
    words = text.split()

    total = len(words) if len(words) > 0 else 1

    lengths = [len(s.split()) for s in sentences]
    avg_sentence_length = np.mean(lengths) if lengths else 0

    lexical_diversity = len(set(words)) / total

    counts = Counter(words)
    repetition = sum(c - 1 for c in counts.values() if c > 1) / total

    simplicity = 1 / (1 + avg_sentence_length)

    fatigue_score = (
        0.35 * (1 - lexical_diversity) +
        0.30 * repetition +
        0.20 * simplicity +
        0.15 * (1 - avg_sentence_length / 20)
    )

    fatigue_score = max(0, min(1, fatigue_score))

    return {
        "avg_sentence_length": avg_sentence_length,
        "lexical_diversity": lexical_diversity,
        "repetition_score": repetition,
        "simplicity_score": simplicity,
        "fatigue_score": fatigue_score
    }
