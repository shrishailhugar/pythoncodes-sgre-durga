# import speech_recognition as sr
# file_name='C:\\Users\\shrishail.hugar.ext\\Downloads\\Recording.wav'
# r=sr.Recognizer()
# with sr.AudioFile(file_name) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_sphinx(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error: {0}".format(e))
