# Q&A Chatbot

from dotenv import load_dotenv

load_dotenv()  

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai




def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text



st.set_page_config(page_title="Advanced ChatBot")

st.header("Ask Storm....")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")



if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
