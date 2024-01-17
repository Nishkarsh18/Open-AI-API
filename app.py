import streamlit as st 
import os
from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"] = "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"
st.set_page_config(page_title='Languagechain Model' , page_icon = ":robot:")
st.header('Welocome to LangChain Project')
def load_answer(ques):
    llm = OpenAI(model_name = "gpt-3.5-turbo-instruct")
    res = llm(ques)
    return res
def get_text():
    input_text = st.text_input("You: " , key = "input")
    return input_text
user_input = get_text()
submit = st.button('Generate')
if submit:
    if(user_input!=''):
        response = load_answer(user_input)
        st.subheader("Answer: ")
        st.write(response)
    else:
        st.write('cannot be empty')
