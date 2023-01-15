import speech_recognition as sr
from tkinter import *
from tkinter import ttk
from jake import Jake
from features import Features
import threading
import os

class Assistant():

    """
    Main Class of this Project
    """

    def __init__(self):
        self.r = sr.Recognizer()
        self.jake = Jake()
        self.features = Features()

        #create a tkinter root
        self.root = Tk()

        #create window title 
        self.root.title("Jake Voice Assistant")
        #create the UI of jake
        self.label = ttk.Label(text="😈", font=("Arial", 120, "bold"))
        self.label.pack()
        
        #create and start a separate thread for self.start method
        self.assistant_thread = threading.Thread(target=self.start)
        self.assistant_thread.start()

        #create a window listener for exit event
        self.root.protocol("WM_DELETE_WINDOW", self.kill)

        #to start tkinter
        self.root.mainloop()

    def start(self):

        """
        Starts the Voice Assistant
        """

        #create infinite loop for voice assistant to always listen.
        while True:
            print("Listening...")
            recognized_audio_str = self.jake.listen()

        #Introduction of Jake  , the smart voice assistant.

            try:
                #trigger exit program
                if "goodbye" in recognized_audio_str:
                    self.jake.say("Thank you, goodbye!")
                    self.kill()

                #trigger jake's features
                if "hey jake" in recognized_audio_str:
                    self.label.config(foreground="red")

                    #Respond of jake
                    print("What can I do for you?")
                    self.jake.say("What can I do for you?")
                    recognized_audio_str = self.jake.listen()
                    try:
                    
                        #process command from recognized audio 
                        self.process_command(recognized_audio_str)
                        
                    #if the commands didn't follow
                    except:
                        print("Error")
        
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #to stop program
    def kill(self):
        print("Goodbye :)")
        self.root.destroy()
        os._exit(1)

    #list of conditions to trigger features
    def process_command(self, command_str):
        if "tell me about yourself" in command_str:
            self.jake.say(
                "I am jake, a voice assistant created by my creator, Ivan. I was made to assist him doing his "
                "final project.")
            print(
                "I am jake, a voice assistant created by my creator, Ivan. I was made to assist him doing his "
                "final project.")
            return

        if "how old are you" in command_str:
            self.jake.say("My creator is eighteen years old. Don't ask about my age because Iam a robot.")
            print("My creator is eighteen years old. Don't ask about my age because Iam a robot.")
            return

        if "show me something" in command_str:
            self.jake.say("I can talk to you and I can be your friend.")
            print("I can talk to you and I can be your friend.")
            return
        
        if "can you sing" in command_str:
            self.jake.say("hahaha no, i am a robot, i have no skills.")
            print("hahaha no, i am a robot, i have no skills.")
            return

        if "i love you" in command_str:
            self.jake.say("i am a robot. I have no feelings, but i love you too.")
            print("i am a robot. I have no feelings, but i love you too.")
            return

        if "turn on the lights" in command_str:
            self.jake.say("i have no hands, apologize.")
            print("i have no hands, apologize.")
            return

        if "why are you so annoying" in command_str:
            self.jake.say("i am you and you are me, so you are also annoying, hahaha.")
            print("i am you and you are me, so you are also annoying, hahaha.")
            return

        if "can you predict the future" in command_str:
            self.jake.say("no, i am not a wizard.")
            print("no, i am not a wizard.")
            return

        if "are you smart" in command_str:
            self.jake.say(
                "i am smart enough to answer you. I will have more features and functions by time." 
                "i hope you live long enough to see me improve.")
            print(
                "i am smart enough to answer you. I will have more features and functions by time."
                "i hope you live long enough to see me improve.")
            return


        #Special Features inside Jake (using external libraries)


        if "what date is today" in command_str:
            today = self.features.tellDate()
            self.jake.say(today)
            print(today)
            return

        if "search" in command_str:
            self.jake.say("What do you want to know?")
            recognized_audio_str = self.jake.listen()

            search_result = self.features.searchWithWikipedia(recognized_audio_str)
            self.jake.say(search_result)
            print(search_result)
            return

        if "entertain me" in command_str:
            quoters = self.features.tellQuote()
            self.jake.say(quoters)
            print(quoters)
            return

        if "show me the weather" in command_str:
            self.jake.say("Which city's weather do you want to know about?")
            recognized_audio_str = self.jake.listen()

            weather_result = self.features.getCurrentWeather(recognized_audio_str)

            print(weather_result)
            self.jake.say(weather_result)
            return

        if "note" in command_str:
            self.jake.say("Yes sir")

            self.features.openNotepad()
            return


Assistant()
