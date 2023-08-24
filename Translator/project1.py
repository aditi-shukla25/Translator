import speech_recognition as spr
from translate import Translator
from gtts import gTTS
import os
 
 
recog1 = spr.Recognizer()
 
mc = spr.Microphone()
 
# Capturing voice
with mc as source:
    print("Speak 'hello' to initiate the Translation !")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    recog1.adjust_for_ambient_noise(source, duration=0.2)

    audio = recog1.listen(source)

    MyText = recog1.recognize_google(audio)
    MyText = MyText.lower()
 
# Check for hello
if 'hello' in MyText:
     
    translator =Translator( to_lang = 'hi',from_lang = 'en' )
     
   
    #The audio which needs to be translated/ Recognition of audio and converting it to text
    with mc as source:
         
        print("Speak a stentence...")
        recog1.adjust_for_ambient_noise(source, duration=0.2)
         
        audio = recog1.listen(source)
         
        get_sentence = recog1.recognize_google(audio)


        #Translation using try and except
        try:
             
            print("Phase to be Translated :"+ get_sentence)
 
            text_after = translator.translate(get_sentence)
             
        
            
            #Using google text to speech to convert the translated text to speech
            speak = gTTS(text=text_after, lang='hi', slow= False)
 
            speak.save("captured_voice.mp3")    
            
            os.system("start captured_voice.mp3")
 
        #using error handling for better experience to user
        except Exception as e:
            print("Translation Error: ", e)
        except spr.UnknownValueError:
            print("Unable to Understand the Input")
             
        except spr.RequestError as e:
            print("Unable to provide Required Output".format(e))