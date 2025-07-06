import requests
import warnings
from transformers import pipeline
from IPython.display import Audio
from transformers.utils import logging
from IPython.display import Audio

global pipe
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
    device="cpu",  # Change to "cuda" if you have a GPU and the model supports it
    chunk_length_s=30,  # Process audio in chunks of 30 seconds
    return_timestamps=True,
)


def download_audio_file(url=""):
    """
    Downloads an audio file from the specified URL and saves it to a local file.

    :param url: The URL of the audio file to download.
    :return: None
    """
    print(f"Downloading audio file from {url}...")
    response = requests.get(url)

    file_name = url.split("/")[-1]  # Extract the file name from the URL

    if response.status_code == 200:
        # If successful, write the content to a local file
        with open(file_name, "wb") as file:
            file.write(response.content)
        print("File downloaded successfully")
    else:
        print("Failed to download file")

        return file_name


def generate_test_from_speech(transcript):
    """
    Generates a test from the speech in the audio file.

    :param audio_file: The path to the audio file.
    :return: None
    """

    text = pipe(transcript)

    # Placeholder for actual speech-to-text processing
    # print(f"Transcribed text: {text}")

    return text["text"]


# logging.set_verbosity_error()
# warnings.filterwarnings("ignore", category=UserWarning)
# download_audio_file(
#     url="http://www.moviesoundclips.net/movies1/darkknightrises/darkness.mp3"
# )
# Audio("Download.mp3", autoplay=True)
# generate_test_from_speech()
