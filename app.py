import os
import whisper
import streamlit as st

from tempfile import NamedTemporaryFile


# Specify the Multilingual model type. Default is "small"
def transcribe_audio(audio_file, model="small") -> tuple:
    model = whisper.load_model(model)
    result = model.transcribe(audio_file)
    return result["text"], result["segments"], result["language"]


# Specify the Multilingual model type. Default is "small"
def translate_to_english(audio_file, model="small") -> tuple:
    model = whisper.load_model(model)
    result = model.transcribe(audio_file, task="translate")
    return result["text"], result["segments"], result["language"]


def milliseconds_to_timestamp(milliseconds) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


def generate_timestamp(segments) -> str:
    timestamp_text = []
    for segment in segments:
        start_time = milliseconds_to_timestamp(int(segment["start"]) * 1000)
        end_time = milliseconds_to_timestamp(int(segment["end"]) * 1000)

        timestamp_text.append(f"[{start_time} --> {end_time}]\n{segment['text']}\n\n")

    return "".join(timestamp_text)


def main() -> None:
    st.title(":green[Whisper App]")

    audio_file_extensions = ["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm", "flac"]
    audio_file = st.file_uploader(":green[Upload audio file to transcribe]",
                                  type=audio_file_extensions)
    if audio_file:
        st.audio(audio_file.read())

        with NamedTemporaryFile(delete=False) as temp_audio:
            temp_audio.write(audio_file.getvalue())
            audio_path = temp_audio.name

        st.write("")
        if st.button("Transcribe Audio"):
            text, segments, language = transcribe_audio(audio_path)
            if text and segments and language:
                st.success("Transcription Successful!")
                st.write(f":green[Detected Language:] {language}")
                st.write(f":green[Transcribed Text:] {text}")
                st.write(f":green[Text with timestamps:] \n\n{generate_timestamp(segments)}")
            # Hopefully it's never reached. Haha!
            else:
                st.error("Transcription Failed!")

        st.write("")
        if st.button("Translate Audio"):
            text, segments, language = translate_to_english(audio_path)
            if text and segments and language:
                st.success("Translation Successful!")
                st.write(f":green[Detected Language:] {language}")
                st.write(f":green[Translated Text:] {text}")
                st.write(f":green[Text with timestamps:] \n\n{generate_timestamp(segments)}")

        # Delete the temporary file after we're done with them
        os.unlink(audio_path)


if __name__ == "__main__":
    main()
