import streamlit as st
import openai
from gtts import gTTS
from io import BytesIO

# Set the OpenAI API key
openai.api_key = st.secrets["api_key"]

# Initialize chat history with a prompt for poem generation
messages = [ 
    {"role": "system", "content": "You are a helpful assistant. Please respond with a poem related to the user's prompt."}, 
]

st.markdown("<h1 style='text-align: center; color: blue;'>Poem Generation Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: blue;'>Enter a prompt and receive a poem</h3>", unsafe_allow_html=True)

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
    global messages
    user_input = st.text_input("Enter a prompt:", placeholder="Enter the text here")
    generate_button = st.button("Generate Poem")

    if generate_button and user_input:
        # Add user input to chat history
        messages.append({"role": "user", "content": user_input})
        
        # Generate response using OpenAI API
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=messages
        )
        poem = response["choices"][0]["message"]["content"]
        
        # Add system response to chat history
        messages.append({"role": "system", "content": poem})

        # Display the generated poem
        st.write("**Generated Poem:**")
        st.write(poem)

        # Convert poem to speech and play audio
        st.audio(text_to_speech(poem), format="audio/wav")

chatbot()
