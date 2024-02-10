import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd

def count_keywords(url, keywords):
    # Fetch HTML content from URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Get the text from the HTML body
    body_text = soup.get_text()
    
    # Count occurrences of each keyword
    keyword_counts = {}
    for keyword in keywords:
        count = body_text.lower().count(keyword.lower())
        keyword_counts[keyword] = count
    
    return keyword_counts

def main():
    st.title("Keyword Counter")
    
    # Sidebar input for URL and keywords
    url = st.sidebar.text_input("Enter URL")
    keyword_input = st.sidebar.text_area("Enter List of Keywords (comma-separated or One keyword per line)")
    keywords = [keyword.strip() for keyword in keyword_input.split("\n") if keyword.strip()]
    
    if st.sidebar.button("Fetch"):
        if not url:
            st.error("Please enter a URL")
        elif not keywords:
            st.error("Please enter at least one keyword")
        else:
            keyword_counts = count_keywords(url, keywords)
            df = pd.DataFrame(list(keyword_counts.items()), columns=['Keyword', 'Count'])
            st.table(df)

if __name__ == "__main__":
    main()
