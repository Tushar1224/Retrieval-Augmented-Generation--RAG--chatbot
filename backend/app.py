# backend/app.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from rag import generate_answer

import streamlit as st


class QueryRequest(BaseModel):
    query: str



#streamlit app

st.set_page_config(page_title='I can Retrieve any SQL query')
st.header("Gemini Chat based application for Medical queries")
questions = st.text_input("Input: ", key="input")
submit = st.button("Ask the questions")



#if submit is clicked
if submit:
    data= generate_answer(questions)
    st.subheader("The Response is ")
    st.write(data)
    # table=pd.DataFrame(updated_result, columns=updated_header)
    # table.index +=1
    # st.dataframe(table)