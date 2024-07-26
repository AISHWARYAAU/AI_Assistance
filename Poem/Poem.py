import streamlit as st
import openai
from gtts import gTTS
from io import BytesIO

# Set the OpenAI API key
openai.api_key = st.secrets["api_key"]

# Define the background image for the app
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1488415032361-b7e238421f1b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2069&q=80");
            background-attachment: fixed;
            background-size: cover;
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

# Display title and instructions
st.markdown("<h1 style='text-align: center; color: white;'>Poem-Writing Tool</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Enter a prompt and receive a poem</h3>", unsafe_allow_html=True)

def text_to_speech(text):
    """
    Converts text to an audio file using gTTS and returns the audio file as binary data.
    """
    audio_bytes = BytesIO()
    tts = gTTS(text=text, lang="en")
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes.read()

def chatbot():
    user_input = st.text_input("Enter a prompt:", placeholder="Enter the text here")
    generate_button = st.button("Generate Poem")

    if generate_button and user_input:
        # System message instructs the AI to respond with a poem
        messages = [
            {"role": "system", "content": "You are a helpful assistant. Please respond with a poem related to the user's prompt."},
            {"role": "user", "content": user_input}
        ]
        
        # Generate response using OpenAI API
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=messages
        )
        poem = response["choices"][0]["message"]["content"]

        # Display the generated poem
        st.write("**Generated Poem:**")
        st.write(poem) 

        # Convert poem to speech and play audio
        st.audio(text_to_speech(poem), format="audio/wav")

chatbot()

