# This is a sample Python script.
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:11:45 2022

@author: Amandeep Verma
"""

# Importing Libararies
import streamlit as st
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
def add_bg_from_url():
  st.markdown(
    f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1505682499293-233fb141754c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2071&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         [data-testid="stHeader"] {{
         background-color: rgba(0,0,0,0);
         }}
         [data-testid="stSidebar"] {{
         background-image: url("https://images.unsplash.com/photo-1487528742387-d53d4f12488d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1922&q=80");
         background-size: cover;
         }}
         </style>

         """,
    unsafe_allow_html=True
  )


add_bg_from_url()




st.title("Text Summarization")
st.header("Summary Generator")

text = st.text_area("Enter your text here.",height=200)
re = len(text.split())
st.markdown("Number of words in text:")
st.write(re)

if st.button("Generate Summary"):
    # Tokenising the text
    nltk.download("stopwords")
    stop_words = stopwords.words('english')
    words = word_tokenize(text)

    punctuation = punctuation + '\n'

    # Creating the Frequency table
    textfreq = {}
    for word in words:
        if word.lower() not in stop_words:
            if word.lower() not in punctuation:
                if word not in textfreq.keys():
                    textfreq[word] = 1
                else:
                    textfreq[word] += 1


    # To find the weighted frequency
    maximum_frequncy = max(textfreq.values())

    for word in textfreq.keys():
        textfreq[word] = (textfreq[word] / maximum_frequncy)

    # Tokenizing the text into sentences
    sentences = sent_tokenize(text)

    # Calculating the score of sentences
    sent_score = {}
    for sent in sentences:
        sentence = sent.split(" ")
        for word in sentence:
            if word.lower() in textfreq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = textfreq[word.lower()]
                else:
                    sent_score[sent] += textfreq[word.lower()]


    # creation of summary
    from heapq import nlargest

    sentlength = int(len(sentences) * 0.3)

    summary = nlargest(sentlength, sent_score, key=sent_score.get)
    final_summary = [word for word in summary]

    summary = ' '.join(final_summary)

    st.write(summary)
    res = len(summary.split())
    st.markdown("Number of words in Summary:")
    st.write(res)