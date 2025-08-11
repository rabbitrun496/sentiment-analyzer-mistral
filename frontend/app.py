import streamlit as st
import requests

st.title("Sentiment Analyzer (Mistral)")

text_input = st.text_area("Enter your sentence here:")

if st.button("Analyze"):
    if text_input.strip():
        try:
            res = requests.post("http://localhost:8000/analyze/", data={"text": text_input})
            res.raise_for_status()  # Raises error for bad HTTP responses
            sentiment = res.json().get("sentiment", "No sentiment returned")
            st.subheader("Predicted Sentiment:")
            st.success(sentiment)
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to analyze.")
