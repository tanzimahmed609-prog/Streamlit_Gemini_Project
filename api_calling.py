from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import os,io
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def note_generator(images):
    prompt = """You are a study assistant. Look at the image(s) and write a short note in 50 words"""
    
    response = client.models.generate_content(
        model = "gemini-3.1-flash-lite",
        contents = [images,prompt]
    )
    return response.text

def audio_generator(text):
    clean = text.replace("*"," ").replace("#"," ").replace(".","  ").replace(","," ")
    speech = gTTS(clean,lang='en',slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer

def quiz_generator(images,difficulity):
    prompt = f"Generate 5 quizzes based on {difficulity}"
    """Make sure to markdown for different options"""
    

    response = client.models.generate_content(
             model = "gemini-3.1-flash-lite",
             contents = [images,prompt]
         )
    return response.text
    