from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
import streamlit as st

genai.configure(api_key=GOOGLE_API_KEY)

model=genai.GenerativeModel('gemini-2.5-flash')
chat=model.start_chat(history=())

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Travel Guru")
st.header("Gemini Application for Travelling")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input1=st.text_input("How is your mood?: ",key="mood_input")
input2=st.text_input("Your favourite food??: ",key="taste_input")
input3=st.text_input("What type of locations you like(mountains,beach etc)??: ",key="location_input")
input4=st.text_input("Things you want to say: ",key="your_prompt")
submit=st.button("Suggest place all over the world")
prompt=f'Generate 5 places in the world for vacation with few details if {input1} is mood and {input2} is type of food and {input3} is type of location and my conditions are {input4}'

if submit and input1 or input2 or input3 or input4:
    response = get_gemini_response(prompt)
    st.session_state['chat_history'].append(("You", prompt))
    st.subheader("The Response is")

    placeholder = st.empty()
    full_response=""
    for chunk in response:
        full_response +=chunk.text
        placeholder.markdown(full_response)
    #st.write(full_response)
    st.session_state['chat_history'].append(("Bot", full_response))

st.subheader("The Chat History is")

for role, text in st.session_state['chat_history']:

    st.write(f"{role}: {text}")
