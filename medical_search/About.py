import streamlit as st
import logging

logging.basicConfig(level=logging.DEBUG)
logging.info("JHU_Streamlit_Demo is starting")
st.set_page_config(
    page_title="Q&A over PDF documents",
    page_icon='app/images/logo.png',
)

cols = st.columns([13, 87])
with cols[0]:
    st.image('app/images/logo.png')
with cols[1]:
    st.title('Q&A over PDF documents')
st.image('app/images/architecture.png')
st.markdown('''
    ### About
    This demo illustrates the use of Gen App Builder Enterprise Search to perform document retrieval and question 
    answering with citation on a biomedical corpus. It allows researches to quickly verify generated answers 
    via the presentation of relevant source materials.
    
    ### Enterprise Search
    The use of Enterprise Search provides powerful functionality out of the box:
    1. It not only fetches the most relevant documents, it also identifies the most relevant snippets within each 
    document.
    2. It feeds the relevant snippets into an LLM and generates a summary answer. In effect it is combining 
    both extractive document retrieval with generative summarization.     
''')
