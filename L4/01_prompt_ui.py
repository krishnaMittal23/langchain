# streamlit run prompt_ui.py 

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


st.header("Research Tool")

user_input = st.text_input("Enter your prompt")
 
if st.button("Ask"):
    result = model.invoke(user_input)
    st.write(result.content)

