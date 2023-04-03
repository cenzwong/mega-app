from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import pyperclip


"""
# NLP AI21Lab App

"""


with st.form("my_form"):
   result_json = {}
   key = st.text_input('Bring your own API Keys', 'jc5dvUcu1UVpWxqMcBCEUUUpFyVUrkvvvv')
   txtParaphrase = st.text_input('Paraphrase', '')

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
      result = requests.post(f"http://localhost:8088/ai21/paraphrase/?text={txtParaphrase}&intent=general&key={key}")

      st.json(result.json(),expanded=False)
      
      result_json = result.json()
      # submitted = False

# responses = st.radio(
#     "Response",
#     result_json)
# st.write(f'<script>navigator.clipboard.writeText({responses});</script>', unsafe_allow_html=True)

for resp in result_json:
   st.code(resp, language="ignore")