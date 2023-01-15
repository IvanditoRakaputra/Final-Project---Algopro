import speech_recognition as sr
import pyttsx3

class Jake ():

    def __init__(self):
        self.ttsEngine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.sr = sr

    def say(self, strToSay):
        """
        The respond of Jake
        """
        #use text to speech engine to output audio
        self.ttsEngine.say(strToSay)
        self.ttsEngine.runAndWait()

    def listen(self):
        """
        Listen for audio from user microphone
        """

        # Use microphone as audio source

        try:
            with sr.Microphone() as source:
                audio = self.r.listen(source)

                # use google's service to process audio input

                recognized_audio_str = self.r.recognize_google(audio)
                recognized_audio_str = str.lower(recognized_audio_str)
                return recognized_audio_str

        except: 
        #if the audio couldn't understand the voice, the program ask to type it. 
            message = "I couldn't understand what you said, could you please type it out for me"

            print(message)
            self.say(message)

            #ask user for input
            command_str = input("Type here: ")
            return command_str
