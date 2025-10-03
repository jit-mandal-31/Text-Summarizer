# app.py
import streamlit as st
from transformers import pipeline

# Load summarizer model once (cached for speed)
@st.cache_resource
def load_summarizer():
    # Force model to run on CPU to avoid "meta tensor" error
    return pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

summarizer = load_summarizer()

# Streamlit UI
st.title("📰 Text Summarizer (3 Sentences)")
st.write("Paste any news article or blog post below, and get a concise summary in 3 sentences.")

# Text input
article = st.text_area("Enter the article/blog text here:", height=300)

if st.button("Summarize"):
    if article.strip():
        # Generate summary using Hugging Face model
        summary = summarizer(article, max_length=130, min_length=30, do_sample=False)

        # Take only 3 sentences
        three_sentence_summary = " ".join(summary[0]['summary_text'].split(". ")[:3]) + "."

        # Show result
        st.subheader("📌 Summary:")
        st.write(three_sentence_summary)
    else:
        st.warning("⚠️ Please paste some text to summarize.")
