import gradio as gr
from speech_to_text import generate_test_from_speech
from speech_to_text import download_audio_file
from llm_processes import generate_summary
import os


def gen_text_from_aud_and_summarize(file_path):
    """
    Function to generate text from audio and summarize it.
    """

    # Generate text from the audio
    transcription = generate_test_from_speech(file_path)
    summary = generate_summary(transcription)
    return transcription, summary


def main():

    # Download the audio file
    audio_path = download_audio_file(
        "http://www.moviesoundclips.net/movies1/darkknightrises/darkness.mp3"
    )

    audio_input = gr.Audio(sources="upload", type="filepath")  # Audio input
    output_text = gr.Textbox()

    iface = gr.Interface(
        fn=gen_text_from_aud_and_summarize,
        inputs=gr.Audio(type="filepath", label="Upload Audio"),
        outputs=[
            gr.Textbox(label="Transcription"),
            gr.Textbox(label="Summary"),
        ],
        title="Audio Transcription + Translation",
        description="Upload an audio file to get both transcription and its Hindi translation.",
        examples=[f for f in os.listdir() if f.endswith(".mp3")],
    )

    iface.launch(server_name="127.0.0.1", server_port=7860)


if __name__ == "__main__":
    main()
