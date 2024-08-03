from langchain_openai import ChatOpenAI
import streamlit as st

st.title("Ask Anything")

with st.sidebar:
    st.title("Add Your API Key First")
    openai_key = st.text_input("OpenAI API Key", type="password")
if not openai_key:
    st.info("Enter your OpenAI API Key to continue")
    st.stop()

llm=ChatOpenAI(model="gpt-4o", api_key=openai_key)


question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)