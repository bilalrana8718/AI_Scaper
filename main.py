import streamlit as st
import scraper as sc
from parser import parse_with_ollama

st.title("Web Scraper")

url = st.text_input("Enter the URL")

if st.button("Start Scraper"):
    st.write("Scraper started")

    result = sc.scrape_website(url)
    body_content = sc.extract_body(result)
    cleaned_body = sc.clean_body(body_content)

    st.session_state.dom_content = cleaned_body

    with st.expander("View Dom Content"):
        st.text_area("DOM content", cleaned_body, height=300)

    print(cleaned_body)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse", height=200)
    if st.button("Parse Content"):
        if parse_description:
            st.write("parsing content")
            dom_chunks = sc.split_dom(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
        


