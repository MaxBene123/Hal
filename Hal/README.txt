Ok unfortunate TA who has to grade my work, imma lay out a step by step process on how to get this shit up and running if you care enough (it is kinda cool tho).
If you dont, there will be a video of it working attached to the work so you can just look at that. 

***THIS PROGRAM REQUIRES 8GB OF VRAM OR MORE***
otherwise the model wont be able to run on your pc :/

***Warning: this code is buggy at the best of times, if something goes wrong, just press the run button again to interupt the program and then run it again***

----Setup----

First, your gonna need ollama on your computer:
-Download Ollama (https://ollama.com/download)
-Wait to finish.
-go to cmd prompt and run the following commands
1. "ollama serve" (might already be running if you clicked on the ollama app, you can check at http://localhost:11434/)
2. "ollama pull deepseek-r1"
now wait for that to download (might be a few mins)

Now, you'll need the dependencies:
-RealtimeSTT
-asyncio
-python_weather
-ollama
-openai
-spotipy

Got all that? Great, just a few more things.

If you want spotify to work, you will need to go to spot.py and set the variables to your personal spotify ID
you will need to set:
-username
-clientID
-clientSecret

Then, you need to authenticate the application via spotify itself. im pretty sure it prompts you to accept or decline but its been a while so im not 100% sure.

Great! Now you should be good to go. run the "interactive.py" file and wait for it to print "say something..." then you should be good to go.

you should notice that if you talk into your microphone, it will print the text to the terminal but do nothing.
however, if you call the AI's name (currently set to Jarvis), it will respond to you.

it has two functions, spotify and weather. 

Eg:
User: "Jarvis, play Three little birds"
Response: "now playing Three Little Birds by Bob Marley [#]play:three little birds~track"

but it will only read out the text part to your chosen speakers (not the command)

Eg 2:
User: "Jarvis, how does the weather look?"
Response: "checking weather now [#]weather"
Response: "It's a perfect 72 degrees outside in golden right now"