import ollama
from openai import OpenAI
from pygame import mixer
from RealtimeSTT import AudioToTextRecorder
import os
import time
from prompt import systemprompt
import sys


client = OpenAI()
mixer.init()


def askquestionmemory(question, model):
    completion = ollama.chat(model=model, messages=[
  {
    'role': 'system',
    'content': systemprompt,
  },
  {
    'role': 'user',
    'content': question,
  },
])
    response = completion['message']['content']
    return response

def terminate():
    sys.exit(0)

def generateTTS(sentence, speechfilepath):
    response = client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=sentence)
    response.stream_to_file(speechfilepath)
    return speechfilepath
    


def play_sound(filepath):
    mixer.music.load(filepath)
    mixer.music.play()
    
        

def TTS(text):
    filepath = generateTTS(sentence=text, speechfilepath="speech.mp3")
    play_sound(filepath)
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.music.unload()
    os.remove(filepath)
    return "done"
    


