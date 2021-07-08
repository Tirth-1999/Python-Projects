import pyttsx3
import speech_recognition as sr

def texttospeech(content):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    engine.say(content)
    engine.runAndWait()

def speechtotext():
    r = sr.Recognizer()
    def SpeakText(command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    while(1):	
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("Did you say '"+MyText+"'")
                SpeakText(MyText)
                if MyText == "stop":
                    return None
                elif MyText == "speech to text" or MyText == "text to speech":
                    return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
            


if __name__ == "__main__":
    print("What do you want to do : 'Speech to Text' or 'Text to Speech'")
    choice = speechtotext()
    if choice == 'speech to text':
        speechtotext()
    else:
        text = str(input("Please Enter text to speak : "))
        texttospeech(text)
    

    