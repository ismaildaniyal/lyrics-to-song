from dotenv import load_dotenv
import requests
import streamlit as st
import whisper
import os
import google.generativeai as genai
from gtts import gTTS

# Configure API Key
load_dotenv()
GEMINI_API_KEY = os.getenv("gemini_api_key")

# Load Whisper AI (Speech-to-Text)
model = whisper.load_model("small")

# Gemini AI Model
genai.configure(api_key=GEMINI_API_KEY)
model1 = genai.GenerativeModel("gemini-1.5-flash")

# Function to Improve Lyrics using Gemini AI
def improve_lyrics_with_gemini(lyrics, genre, language):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{"parts": [{"text": f"Convert these lyrics into a well-structured {genre} song in {language}: {lyrics}"}]}]
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        else:
            return f"API Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to send lyrics to Suno AI
def generate_song_with_suno(lyrics):
    try:
        url = "https://api.sunoapi.com/generate-song"  # Replace with actual Suno AI API endpoint
        headers = {"Authorization": f"Bearer {os.getenv('SUNO_API_KEY')}"}
        data = {"lyrics": lyrics}

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json().get("song_url", "Error retrieving song")
        else:
            return f"API Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

st.title("🎵 AI Lyrics-to-Song Generator")
st.write("Upload your voice or type lyrics, and AI will generate a full song!")

# Select Genre and Language
genre = st.selectbox("🎼 Choose Genre:", ["Pop", "Rap", "Jazz", "Rock", "EDM"])
language = st.selectbox("🗣 Choose Language:", ["English", "Spanish", "French", "Hindi", "Chinese"])

# File Upload Option for Audio
st.write("🎤 Upload your audio below:")
audio_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

if audio_file is not None:
    temp_audio_path = "temp_audio.wav"
    with open(temp_audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

    if st.button("Process Uploaded Audio"):
        st.write("🔍 Transcribing lyrics...")
        result = model.transcribe(temp_audio_path)
        transcription = result["text"]
        detected_lang = result["language"]

        st.write(f"📝 **Detected Lyrics:** {transcription}")
        st.write(f"🌍 **Detected Language:** {detected_lang}")

        # Improve lyrics with Gemini AI
        st.write("🎶 Enhancing lyrics with AI...")
        improved_lyrics = improve_lyrics_with_gemini(transcription, genre, language)
        st.write(improved_lyrics)

        # # Generate song using Suno AI
        # st.write("🎼 Generating song with Suno AI...")
        # song_url = generate_song_with_suno(improved_lyrics)
        
        # if "Error" not in song_url:
        #     st.audio(song_url, format="audio/mp3")
        #     st.write("✅ **Song generated successfully!**")
        #     st.download_button("⬇ Download AI-Generated Song", song_url)
        # else:
        #     st.write("❌ Error generating song: ", song_url)

        # Export Lyrics
        lyrics_path = "song_lyrics.txt"
        with open(lyrics_path, "w") as file:
            file.write(improved_lyrics)

        st.download_button("⬇ Download Lyrics", lyrics_path)

        # Cleanup temporary files
        os.remove(temp_audio_path)
