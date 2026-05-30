
# 🧠 Behavioral Volatility Index (BVI)

A modular NLP and behavioral modeling system that quantifies **text-based psychological volatility** by combining linguistic fingerprinting, cognitive fatigue estimation, and sentiment dynamics.

The system processes natural language sequences to output a unified metric called the **Behavioral Volatility Index (BVI)**, mapping how an individual's underlying behavioral stability shifts under prolonged mental stress.


## Project Objective

This project explores how **language reflects behavioral instability under cognitive load**. By analyzing digital text footprints, the engine maps:
* **Emotional Strain:** Fluctuations in immediate sentiment and psychological tone.
* **Linguistic Complexity:** Degradation or flattening of structural expression.
* **Social vs. Self-Focus:** Tracking shifts in pronoun density ratios.
* **Compounding Stress:** Modeling how baseline personality traits break down under prolonged fatigue.

The ultimate goal is to simulate a real-time **behavioral risk signal** from unstructured natural language inputs.



## 🏗️ Architecture

```text
       Input Text
           │
           ▼
     Preprocessing  ──────► (Tokenization, Cleaning)
           │
           ▼
  Feature Extraction Layers 
   ├── Personality Profiles ──► (Self-focus, Dominance, Intensity)
   └── Fatigue Estimators   ──► (Repetition patterns, Structural degradation)
           │
           ▼
       BVI Engine   ──────► (Weighted Matrix + Interaction Model)
           │
           ▼
  Explainability Module ──► (Feature Attribution JSON)
           │
           ▼
  Streamlit Dashboard ────► (Real-Time UI & Volatility Tracking)

```


## 📊 Core Features

### 1. Personality Modeling

Extracts implicit linguistic signals from text structure:

* **Self-Focus Ratio:** High-density first-person singular pronouns.
* **Social Focus Ratio:** Collective pronouns indicating group integration.
* **Dominance Indicators & Emotional Intensity:** Volatility profiles across interactions.
* **Lexical Diversity:** Tracking baseline text variability.

### 2. Cognitive Fatigue Estimation

Measures signs of cognitive depletion:

* **Sentence Complexity:** Reductions in clausal structures.
* **Repetition Patterns:** Tracking lexical loops and predictable vocabulary.
* **Structural Degradation:** Simplification scores calculated relative to baseline performance.

### 3. BVI Computation Engine

The system processes features through an interaction model where fatigue acts as a catalyst for baseline psychological traits:

$$BVI = \alpha F + \beta P_{instability} + \gamma (F \times P_{instability})$$

Where:

* $F$ = Fatigue score
* $P_{instability}$ = Baseline personality instability index
* The interaction term $(F \times P_{instability})$ models compounding stress effects over time.

### 4. Explainability Layer

Breaks down the final index into clear component vectors:

* Independent fatigue contribution
* Independent personality contribution
* Compounding interaction effects

### 5. Interactive Streamlit Dashboard

Provides a full frontend interface featuring:

* Real-time BVI score calculation.
* Granular feature breakdowns.
* Explainability JSON outputs.
* Interactive behavioral trend graphs with session-based memory tracking.

---

## 📁 Project Structure

```text
bvi_project/
│
├── app/
│   └── streamlit_app.py        # Dashboard interface and plotting logic
│
├── src/
│   ├── preprocessing.py         # Text cleaning and tokenization pipelines
│   ├── personality_features.py  # Linguistic fingerprinting algorithms
│   ├── fatigue_features.py      # Structural degradation metrics
│   ├── volatility_engine.py     # Core mathematical model execution
│   └── explainability.py        # Matrix breakdown and attribution formatting
│
├── requirements.txt            # Project dependencies
└── README.md                   # System documentation

```

---

## ⚙️ Installation & Usage

### Local Deployment

Install the required python packages:

```bash
pip install -r requirements.txt

```

Boot up the interactive visualization panel locally:

```bash
streamlit run app/streamlit_app.py

```

### Example Output Vector

```json
{
  "fatigue": 0.13,
  "personality_instability": 0.19,
  "interaction": 0.02,
  "BVI": 38.42
}

```

---

## 📉 System Limitations

1. **Heuristic-Based Scoring:** The current model utilizes rule-based feature engineering and is designed for prototyping; it is not trained on clinical psychological datasets.
2. **Interpretive Index:** BVI serves as an algorithmic proxy for behavioral friction and is not a validated clinical metric.
3. **Context Window Limitations:** Optimized for sentence-level or short-text sequence analysis rather than longitudinal conversational histories.
4. **Sentiment Parsing:** Relies on VADER lexicon models, which may exhibit lower accuracy when parsing sarcasm or highly context-dependent slang.

---

## Streamlit Deployment Context

When hosting via cloud runtime tunnels or container environments, note the following configurations:

* **Asset Routing:** Network tunnels (e.g., localtunnel, ngrok) can occasionally interrupt dynamically loaded static JavaScript modules.
* **Session Management:** Default variables stored in `st.session_state` reset upon full container redeployments.
* **Cold Starts:** Initial runs require an execution buffer to load and download active NLTK lexicons.

---

## Future Roadmap

* **Statistical ML Regression:** Transitioning from heuristic weights to models trained on empirical behavioral data.
* **Temporal Modeling:** Implementing sequence architectures (LSTM or Transformers) to capture directional behavioral drift over extended sessions.
* **Advanced Explainability:** Integrating SHAP (SHapley Additive exPlanations) for real-time feature attribution.
* **Multimodal Signals:** Expanding the input pipeline to capture keystroke latency dynamics and voice tone metrics.

---

## Tech Stack

* **Language:** Python
* **User Interface:** Streamlit
* **Natural Language Processing:** NLTK (VADER Sentiment Engine)
* **Data Core:** Pandas, NumPy
* **Visualizations:** Matplotlib

---

## 📌 Author Notes

This project is an experimental behavioral modeling pipeline built for educational and computational research prototyping. It highlights how implicit linguistic features can be translated into interpretable behavioral signals.

```

```
