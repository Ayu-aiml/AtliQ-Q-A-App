import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Apply custom CSS for gradient background and text styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #fbc2eb, #a6c0fe);
        padding: 2rem;
    }
    .stTitle {
        color: #ffffff;
        font-size: 2rem;
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stHeader {
        color: #ffffff;
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)
