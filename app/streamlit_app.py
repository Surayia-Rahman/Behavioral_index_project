
# path setup
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

from src.preprocessing import process_sample
from src.personality_features import extract_personality_features
from src.fatigue_features import compute_fatigue_features
from src.volatility_engine import compute_bvi
from src.explainability import explain_bvi

# nltk safe 
try:
    nltk.data.find("sentiment/vader_lexicon")
except LookupError:
    nltk.download("vader_lexicon")

sentiment_analyzer = SentimentIntensityAnalyzer()

# ui
st.title("Behavioral Volatility Index (BVI)")

# session memory
if "history" not in st.session_state:
    st.session_state.history = []

# input
text = st.text_area("Enter text")

# pipeline
if st.button("Analyze") and text:

    sample = {
        "user_id": "demo",
        "timestamp": len(st.session_state.history),
        "text": text
    }

    processed = process_sample(sample)
    personality = extract_personality_features(processed, sentiment_analyzer)
    fatigue = compute_fatigue_features(processed, personality)
    bvi = compute_bvi(personality, fatigue)
    explanation = explain_bvi(personality, fatigue)

    st.session_state.history.append({
        "bvi": bvi["BVI"],
        "fatigue": bvi["fatigue"],
        "personality": bvi["personality_instability"]
    })

    st.subheader("BVI Score")
    st.metric("Volatility Index", round(bvi["BVI"], 2))

    st.subheader("Breakdown")
    st.json(bvi)

    st.subheader("Explainability")
    st.json(explanation)

# visualization
if len(st.session_state.history) > 1:

    df = pd.DataFrame(st.session_state.history)

    st.subheader("Behavior Over Time")

    fig, ax = plt.subplots()

    ax.plot(df["bvi"], label="BVI")
    ax.plot(df["fatigue"], label="Fatigue")
    ax.plot(df["personality"], label="Personality Instability")

    ax.set_xlabel("Inputs Over Time")
    ax.set_ylabel("Score")
    ax.legend()

    st.pyplot(fig)
