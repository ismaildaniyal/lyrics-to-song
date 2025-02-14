# AI Lyrics-to-Song Generator

## Overview
This project is a **Streamlit-based AI application** that converts voice recordings or typed lyrics into enhanced lyrics and generates a complete song using AI models. It integrates **Whisper AI** for speech-to-text conversion, **Gemini AI** for lyric enhancement, and **Suno AI** for song generation.

## Features
- 🎤 **Speech-to-Text**: Converts uploaded audio into lyrics using OpenAI's Whisper model.
- 🎶 **AI-Powered Lyrics Enhancement**: Improves lyrics based on the selected genre and language with Gemini AI.
- 🎼 **AI Song Generation**: Uses Suno AI to generate a complete song from the improved lyrics.
- 📥 **Downloadable Lyrics**: Allows users to download enhanced lyrics in a text file.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pip` (Python package manager)

### Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/ai-lyrics-generator.git
   cd ai-lyrics-generator
   ```

2. **Create a virtual environment** (optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory and add your API keys:
   ```sh
   gemini=your_gemini_api_key
   SUNO_API_KEY=your_suno_api_key
   ```

5. **Run the Streamlit app**
   ```sh
   streamlit run app.py
   ```

## Usage
1. **Upload an audio file** (`.wav` or `.mp3`).
2. **Select genre and language** for lyric enhancement.
3. **Process the audio** to transcribe lyrics.
4. **View and download** AI-enhanced lyrics.
5. *(Optional)* Generate a song (Suno AI integration).

## Future Enhancements
- 🎵 Add real-time voice recording feature.
- 🎙️ Support for multiple AI models for music generation.
- 🌎 Expand to more languages and music styles.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to improve.

## License
This project is licensed under the **MIT License**.

---
**Author:** M Ismail Daniyal  
🚀 _Transforming lyrics into AI-powered music!_

