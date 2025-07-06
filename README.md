# 🤖 Meeting Summarizer with LLaMA, Whisper & LangChain

A modular, GPU-ready LLM-powered tool that transcribes and summarizes meeting audio files into structured key points using Whisper and LLaMA 3.2 1B-Instruct. Built with Hugging Face Transformers, LangChain, and Gradio for a simple user interface.

---

## 🔧 Features

- 🎙️ Whisper-powered audio-to-text transcription from MP3 files
- 🧠 LLaMA-based summarization using Hugging Face Transformers
- 📑 Structured output with custom prompt template
- 🔗 Integrated with LangChain Expression Language (LCEL)
- ⚡ GPU-compatible with RTX 3050 Ti or any CUDA GPU
- 💬 Gradio web interface for easy user interaction
- 📄 Accepts real meeting audio and text transcripts as input

---

## 🏗️ Project Flow

1. Load MP3 file and transcribe to text using OpenAI Whisper
2. Load LLaMA 3.2 model + tokenizer from Hugging Face
3. Define prompt using LangChain’s PromptTemplate
4. Pipe the prompt into the LLM using LCEL: prompt | llm
5. Call chain.invoke() to generate summary
6. Display output via console or Gradio interface

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/meeting-summarizer.git
cd meeting-summarizer
```

### 2. Install Required Packages

Make sure you have Python 3.10+ and pip installed.

```bash
pip install -r requirements.txt
```

If using a GPU:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

If using CPU only:

```bash
pip install torch
```

### 3. Run the Project

```bash
python main.py
```

Or directly use the summary function:

```python
from llm_processes import summarize_context

text = "Your long meeting transcript goes here..."
print(summarize_context(text))
```

---

## 🧠 Prompt Template

```jinja
<s><<SYS>>
List the key points with details from the context:
[INST] The context : {context} [/INST]
<</SYS>>
```

---

## 🧪 Example Input

Files given in the folder "Test Audios" as :

1. Darkness.mp3
2. Download.mp3

are meant for testing purpose only. Which are downloaded from the given below resources.

- https://media.un.org/avlibrary/en/asset/d341/d3419970 [UN - Audio Visual Library]
- http://www.moviesoundclips.net/movies1/darkknightrises/darkness.mp3 [Movieclips.mp3]

```txt
The weekly team sync was held on Monday to align everyone on project timelines and blockers. Rahul confirmed that the frontend module will be completed by Thursday, while Priya raised a concern regarding delays in the data pipeline...
```

💡 Output:

- Frontend module due Thursday
- Data pipeline blocked by vendor
- Prioritize API integration in parallel
- UI review scheduled for Wednesday
- Sprint retro moved to Friday

---

## 🛠️ Tech Stack

- Python 3.10+
- Hugging Face Transformers
- LangChain (LCEL)
- LLaMA 3.2 (1B) – causal LM
- CUDA/GPU (optional)
- Prompt Engineering
- OpenAI Whisper
- Gradio (UI)

---

## 📁 Project Structure

Folder Miscellaneous contains testing files for ffmpeg & Cuda.
Understand and run appropriately.

```
├── miscellaneous/
    ├── cuda_testing.py
    ├── ffmpeg-testing.py
    └── whisper_transcription.py
├── Test Audios/
    ├── darkness.mp3
    └── Download.mp3
├── llm_processes.py         # Model & prompt logic
├── main.py                  # CLI interface
├── speech_to_text.py          # Example script
├── requirements.txt
└── README.md
```

---

## 💡 Future Additions

- Whisper integration for MP3/WAV audio summarization
- PDF/Docx summarization
- Streamlit UI
- CSV/JSON export of summaries
- RAG-based long memory for multi-meeting context
- Image processing & Graph understanding
- PDF generation with detailed timestamp processing

---

## 👤 Author

Dev Patel  
B.E. in Computer Engineering | AI & GenAI Enthusiast  
GitHub: https://github.com/Destron7
