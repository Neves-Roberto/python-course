
import speech_recognition as sr


def main():
    sound = "C:\\Users\\projetos\\recorder8.wav"

    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)

        print("Converting Audio To Text ..... ")

        audio = r.listen(source)

    try:
        print("Converted Audio Is : \n" + r.recognize_google(audio,language='pt-BR'))


    except Exception as e:
        print("Error {} : ".format(e))


if __name__ == "__main__":
    main()
    
"""
    
import speech_recognition as sr
AUDIO_FILE = ("C:\\Users\\projetos\\recorder.wav")
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("The audio file contains: " + r.recognize_google(audio,language='pt-BR'))

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

try:
    print("The audio file contains: " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

"""