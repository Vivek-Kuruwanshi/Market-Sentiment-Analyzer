# 📈 Market Sentiment Analyzer

A real-time, interactive financial news sentiment analysis dashboard. This application aggregates live RSS news feeds for targeted equities, processes the articles using a deep-learning Natural Language Processing (NLP) pipeline, and visualizes the market mood instantly.

## 🚀 Features
* **Live Ingestion:** Dynamically fetches up-to-date market news using `feedparser`.
* **Deep Learning NLP:** Utilizes Hugging Face `transformers` to perform context-aware sentiment analysis on headline data.
* **Performance Optimized:** Implements Streamlit caching (`st.cache_resource` & `st.cache_data`) to optimize model loading and reduce data fetching latency.
* **Interactive Dashboard:** Built with a dark-mode optimized `streamlit` interface featuring dynamic visual splits powered by `plotly.express`.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Data Wrangling:** Pandas
* **AI/NLP:** Hugging Face Transformers
* **Data Fetching:** Feedparser, Urllib
* **UI & Visualization:** Streamlit, Plotly Express

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Vivek-Kuruwanshi/market-sentiment-analyzer.git](https://github.com/Vivek-Kuruwanshi/market-sentiment-analyzer.git)
   cd market-sentiment-analyzer

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the application locally:**
   ```bash
   streamlit run main.py 
