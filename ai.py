import os
import pyaudio as py
import speech_recognition as sr
from openai import OpenAI



client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()





def speak(quarry):
    os.system(f"say {quarry}")




def capture_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text


while(1):
    inp=capture_voice_input()


    out=chat_gpt(inp)
    if out=="":
        continue
    out.replace("'","")
    print("Assi : ",f'{out}')
    speak(f'{out}')

    if "bye" in inp:
        break

