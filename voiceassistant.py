import speech_recognition as sr
import yagmail
import speech_recognition as sr 
import wikipedia
import pyttsx3

engine=pyttsx3.init()
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise..')
    print('Clearing background noise...Please wait')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for your message...")
    recordedaudio=recognizer.listen(source)
    print('Done recording..!')
    print('Done recording')

try:
    print('Printing the message..')
    print('Printing your message...Please wait')
    text=recognizer.recognize_google(recordedaudio,language='en-US')

    print('Your message:{}'.format(text))
    print('Your Message:{}',format(text))

except Exception as ex:
    print(ex)

#Automate mails:

reciever='queriesakpython@yahoo.com'
message=text
sender=yagmail.SMTP('hs4865900@gmail.com')
sender.send(to=reciever,subject='This is an automated mail',contents=message)
#Input data
wikisearch=wikipedia.summary(text)
engine.say(wikisearch)
engine.runAndWait()