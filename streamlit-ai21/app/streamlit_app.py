from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import pyperclip


"""
# NLP AI21Lab App

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.form("my_form"):
   result_json = {}
   key = st.text_input('Bring your own API Keys', '')
   txtParaphrase = st.text_input('Paraphrase', '')

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
      result = requests.get(f"http://localhost:8088/ai21/paraphrase/hellowolrd?intent=general&key={key}")

      st.json(result.json(),expanded=False)
      
      result_json = result.json()

for resp in result_json:
   st.code(resp)

