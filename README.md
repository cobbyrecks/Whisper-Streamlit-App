## Whisper Streamlit App

This application transcribes and translates audio files using the Whisper library.

### Installation

1. Install PyTorch from [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/).
2. Install ffmpeg based on your operating system.
3. Run `pip install -U openai-whisper` to install the Whisper library.
4. Install Streamlit with `pip install streamlit`.

Note: Refer to [Whisper Repository README](https://github.com/openai/whisper/blob/main/README.md) for detailed installation procedure.

### Usage

1. Upload an audio file in one of the supported formats: mp3, mp4, mpeg, mpga, m4a, wav, webm, flac.
2. Click on "Transcribe Audio" to transcribe the uploaded audio file.
3. Click on "Translate Audio" to translate the transcribed text to English.
4. The application displays the detected language, transcribed or translated text, and text with timestamps.
5. Optionally, specify the desired model type in the `app.py` script to download and use a model of your choice.

### Notice

- The default model for this app is the small Multilingual model. It is downloaded the first time the script is run.
- Users can specify the model type in the `app.py` script to download and use a model of their choice.
