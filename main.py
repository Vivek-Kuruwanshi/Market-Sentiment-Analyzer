import feedparser
import gc
import streamlit as st
import transformers 
import pandas as pd
import urllib.parse
import plotly.express as px

@st.cache_resource(show_spinner="loading financial analysis model please wait")

def load_pipeline():
    return transformers.pipeline(task = "text-classification",model = "ProsusAI/finbert",low_cpu_mem_usage=True)


def generate_main_window():
    st.title("Market Sentiment Analyzer")
    company_name = st.text_input("Enter company name")
    
    if(company_name.strip()):
        st.success(f"you chose {company_name}!!!")
        data = get_market_sentiment(web_scrap_company_summary(company_name))
        
        st.subheader("Market Sentiment Breakdown")
        if(data['negative']==0 and data['positive']==0 and data['neutral']==0):
            st.error("No data found")
        else:
            plot_df = pd.DataFrame({
                "Sentiment":list(data.keys()),
                "Count":list(data.values())
            })
            st.subheader("Data Table View")
            st.dataframe(plot_df.set_index("Sentiment"))

            st.subheader("Bar Graph")

            fig = px.bar(
                plot_df,
                x="Sentiment",
                y="Count",
                color="Sentiment",
                color_discrete_map={"positive":"#10b981","neutral":"#94a3b8","negative":"#ef4444"}
            )
            fig.update_layout(xaxis_tickangle=0)
    
   
            st.plotly_chart(fig, use_container_width=True)

            if(data['positive']+data['negative']<data['neutral']):
                st.warning("Not worth it")
            elif(data['positive']>data['negative']):
                st.success("The company is Bullish")
            else:
                st.error("The company is Bearish")

    else:
        st.error("please enter a valid company name")

def get_sentiment(sentences:list[str])->list[dict]:
    if(len(sentences)==0):
        return []
    finbert = load_pipeline()
    sentiment = finbert(sentences)
    return sentiment
@st.cache_data(ttl=600,max_entries=1)
def get_market_sentiment(summary_related_to_company:list[str])->dict:
    sentiments={"positive": 0, "negative": 0, "neutral": 0}
    market_sentiment = get_sentiment(summary_related_to_company)
    for entry in market_sentiment:
        label = entry.get("label")
        if(label==None):
            continue
        else:
            sentiments[label]+=1
    gc.collect()
    return sentiments


def web_scrap_company_summary(company_name:str)->list[str]:
    query = f"{company_name.strip()}"
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(url)

    summaries = []
    for entry in feed.entries[:50]: 
        if(getattr(entry,"summary","")):
            summaries.append(getattr(entry,"summary",""))
            summaries.append(getattr(entry,"title",""))
    return summaries

if __name__ == "__main__":
    generate_main_window()
