
# Handles text cleaning + segmentation
# Based on psycholinguistic preprocessing principles:
# - Pennebaker LIWC methodology
# - Cognitive load preservation (Sweller 1988)

import re
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = text.strip()
    text = re.sub(r"http\\S+|www\\S+", "", text)
    text = re.sub(r"\\s+", " ", text)
    return text

def segment_sentences(text):
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]

def process_sample(sample):
    text = clean_text(sample["text"])
    sentences = segment_sentences(text)

    return {
        "user_id": sample["user_id"],
        "timestamp": sample["timestamp"],
        "raw_text": sample["text"],
        "clean_text": text,
        "sentences": sentences
    }
