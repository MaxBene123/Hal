import hopeitworks as assist
from RealtimeSTT import AudioToTextRecorder
import time
import spot
import tools
import hopeitworks
import sys

#To do list:
#1. add playing check to spotify start function. if its currently playing something dont do anything but if not, use spotify.start
#2. add more fail safe checks, especally when it comes to commands
#3. update prompt (forever
#4. add puffco API in tools
#5. update playlist option in spotify to reutrn a list of the users playlists and then play one of those. 

model = "deepseek-r1"

if __name__ == '__main__':
    recorder = AudioToTextRecorder(spinner=False, model="medium.en", language="en", post_speech_silence_duration =0.2, silero_sensitivity = 0.4)
    hot_words = ['hal', 'jarvis']
    skip_hot_word_check = False
    print("Hello! Say something...")
    while True:
        current_text=recorder.text()
        print(current_text)
        if any(hot_word in current_text.lower() for hot_word in hot_words) or skip_hot_word_check:
                    #make sure there is text

                    if current_text:
                        if "terminate" in current_text:
                            sys.exit(0)
                        print("User: " + current_text)
                        recorder.stop()
                        #get time
                        current_text = current_text #+ " " + time.strftime("%Y-m-%d %H-%M-%S")
                        response = assist.askquestionmemory(current_text, model=model)
                        print(response)
                        speech = response
                        if model == "deepseek-r1":
                            if "</think>" in speech:
                                speech = speech.split("</think>")[-1]
                        speech = speech.split("[#]")[0]
                        done = assist.TTS(speech)
                        if "?" in speech: 
                            skip_hot_word_check = True
                        else:
                            skip_hot_word_check= False
                        if len(response.split('[#]')) > 1:
                            command = response.split('[#]')[-1]
                            tools.parse_command(command)
                        recorder.start()

