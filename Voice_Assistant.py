from platform import uname
import time
import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition, pip install pipwin & pipwin install pyaudio
import datetime # pip install datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib 
import pyjokes # pip install pyjokes

# initialises the pyttsx3 modules
# Microsoft Speech API (SAPI5) is the technology for voice recognition & synthesis, provided by Microsoft
engine = pyttsx3.init('sapi5')

# it'll get the voice property frm the pyttsx3 module
voices = engine.getProperty('voices')

# it'll get  list of voices & v can select 1 which v lyk
# voices[0].id -> Male voice
# voices[1].id -> Female voice
engine.setProperty('voice', voices[0].id)

# now vll set the voice speed
# by default it will b 200 words per min
engine.setProperty('rate', 190) # 190 words per min

ass_name = "Jarvis"

def speak(audio):
    engine.say(audio) # convert the written text in2 speach
    engine.runAndWait() # pauses the program till the say function is done wyt speaking

def wishMe():
    speak("Welcome back!")

    hour = int(datetime.datetime.now().hour)

    if hour >= 2 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")
    elif hour >= 17 and hour < 23:
        speak("Good Evening!")
    else:
        speak("Good Night!")  

    speak("I'm your Assistant")
    speak(ass_name)
    speak("AI at your service")       

def takeCommand():
    # It takes microphone input frm the user & returns string output

    r = sr.Recognizer() # v r initializing the Recognizer in the r variable
    with sr.Microphone() as source: # get input frm the user frm the microphone, it will our source for our input
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 2 # it will wait for 2 sec before it strt 2 listen
        audio = r.listen(source) # microphone will listen 2 our audio, v hv passed source variable in listen function

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Could not understand audio...")
        speak("Could not understand audio...")
        print("Say that again please...")  
        speak("Say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # enable low security in gmail
    server.login('your emai id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()

    print('What should I call you ?')
    speak('What should I call you ?')
    uname = takeCommand()
    print('Welcome', uname)
    speak('Welcome')
    speak(uname)
    speak('Please tell me how may I help you')

    while True:
    # if 1:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query.replace("wikipedia", ""), sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print('Here you go to YouTube\n')
            speak('Here you go to YouTube\n')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print('Here you go Google\n')
            speak('Here you go Google\n')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            print('Here you go Stackoverflow\n')
            speak('Here you go Stackoverflow\n')
            webbrowser.open("stackoverflow.com")  

        elif 'open github' in query:
            print('Here you go Github\n')
            speak('Here you go Github\n')
            webbrowser.open("github.com")

        elif 'open dev community' in query:
            print('Here you go Dev Community\n')
            speak('Here you go Dev Commmunity\n')
            webbrowser.open("dev.to")

        elif 'open kaggle' in query:
            print('Here you go Dev Kaggle\n')
            speak('Here you go Dev Kaggle\n')
            webbrowser.open("kaggle.com")

        elif 'open protonmail' in query:
            print('Here you go Proton Mail\n')
            speak('Here you go Proton Mail\n')
            webbrowser.open("mail.protonmail.com")

        elif 'open brave' in query:
            print('Here you go Brave Browser\n')
            speak('Here you go Brave Browser\n')
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" # ur brave browser directory
            os.startfile(codePath)

        elif 'open firefox' in query:
            print('Here you go Firefox Browser\n')
            speak('Here you go Firefox Browser\n')
            codePath = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe" # ur firefox browser directory
            os.startfile(codePath)

        elif 'open chrome' in query:
            print('Here you go Chrome Browser\n')
            speak('Here you go Chrome Browser\n')
            codePath = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk" # ur chrome browser directory
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            print('Here you go WhatsApp\n')
            speak('Here you go WhatsApp\n')
            codePath = r"C:\\Users\\Rahul\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp.lnk" # ur whatsapp directory
            os.startfile(codePath)

        elif 'open telegram' in query:
            print('Here you go Telegram\n')
            speak('Here you go Telegram\n')
            codePath = r"C:\\Users\\Rahul\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Telegram Desktop\\Telegram.lnk" # ur telegram directory
            os.startfile(codePath)

        elif 'open jetbrains toolbox' in query:
            print('Here you go Jetbrains Toolbox\n')
            speak('Here you go Jetbrains Toolbox\n')
            codePath = r"C:\\Users\\Rahul\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains Toolbox\\JetBrains Toolbox.lnk" # ur jetbrains toolbox directory
            os.startfile(codePath)

        elif 'open vs code' in query or 'visual studio code' in query:
            print('Here you go VS Code\n')
            speak('Here you go VS Code\n')
            codePath = r"C:\\Users\\Rahul\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk" # ur vs code directory
            os.startfile(codePath)

        elif 'open code' in query:
            print('Here you go Project Code\n')
            speak('Here you go Project Code\n')
            codePath = r"D:\\Projects\\Python Projects\\Voice_Assistant.py" # ur project directory
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2' # ur music directory
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'send a mail to' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                speak("whom should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend, I'm not able to send this email")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time now is {strTime}")

        elif 'how are you' in query:
            print("I'm fine, Thank you")
            speak("I'm fine, Thank you")
            print("How are you,", uname)
            speak("How are you,")
            speak(uname)

        elif 'fine' in query or 'good' in query:
            print("It's good to know that you are fine")
            speak("It's good to know that you are fine")

        elif 'who i am' in query or 'who am i' in query:
            print('If you talk then definitely your human and your name is', uname)
            speak('If you talk then definitely your human and your name is')
            speak(uname)

        elif 'change my name' in query:
            speak('What would you like me to call you ?')
            print('What would you like me to call you ?')
            uname = takeCommand()
            speak('Your name is changed to')
            speak(uname)
            print('Your name is changed to', uname)
            
        elif 'change your name' in query:
            print('What would you like to call me,', uname)
            speak('What would you like to call me,')
            speak(uname)
            ass_name = takeCommand()
            print('Thanks for naming me as', ass_name)
            speak('Thanks for naming me as')
            speak(ass_name)

        elif "what's your name" in query or 'what is your name' in query:
            print('My friends call me', ass_name)
            speak('My friends call me')
            speak(ass_name)

        elif 'what is my name' in query or "what's my name" in query:
            print("Your name is ", uname)
            speak('Your name is')
            speak(uname)

        elif 'who made you' in query or 'who created you' in query:
            print('I have been created by Rahul')
            speak('I have been created by Rahul')

        elif 'exit' in query or 'quit' in query:
            print('Thanks', uname,'for giving me your time')
            speak('Thanks')
            speak(uname)
            speak('for giving me your time')
            exit()

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'why you came to earth' in query or 'why did you come to earth' in query:
            print("Thanks to Rahul, further It's a secret")
            speak("Thanks to Rahul, further It's a secret")
            
        elif 'why have you been created' in query or 'reason for you' in query or 'reason for your creation' in query:
            print('I was created as a project by Mister Rahul')
            speak('I was created as a project by Mister Rahul')

        elif 'where is' in query:
            location = query.replace('where is', '')
            print(uname, 'asked to locate', location)
            speak(uname)
            speak('asked to locate')
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "write a note" in query:
            print('What should I write', uname)
            speak('What should I write')
            speak(uname)
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            print(uname, 'Should I include date and time')
            speak(uname)
            speak("Should I include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm or 'ok' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query or 'open note' in query:
            print("Showing Notes")
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            sleep_time = int(takeCommand())
            time.sleep(sleep_time)
            print(sleep_time)

        # most asked question frm google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            print("I'm not sure about, may be you should give me some time")
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query:
            print("It's hard to understand")
            speak("It's hard to understand")

        # elif "" in query:
			# command go here
			# for adding more commands
