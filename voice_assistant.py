import speech_recognition as SR
import pyttsx3
import pywhatkit
import wikipedia

mark = pyttsx3.init()
def mark_speak(content):
    mark.say(content)
    mark.runAndWait()
    print(content)

listener = SR.Recognizer()
def listen_to_user():
    try:
        mark_speak("Hey there! I'm Mark, your virtual assistant.")
        with SR.Microphone() as source:
            mark_speak("How can I help you?")
            user_audio = listener.listen(source)
            user_input = listener.recognize_google(user_audio).lower()
            if "mark" in user_input:
                print(user_input.upper())
                user_input = user_input.replace("mark","")
    except:
        pass
    return user_input

command = listen_to_user()
if "play" in command:
    command = command.replace("play", "")
    mark_speak("Playing "+command)
    pywhatkit.playonyt(command)
else:
    mark_speak("Searching for"+command)
    info = wikipedia.summary(command,1)
    mark_speak(info)