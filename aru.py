import speech_recognition as sr
import cmd
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot named Aruack
aruack = ChatBot('Aruack')

# Train the chat bot based on the English corpus
trainer = ChatterBotCorpusTrainer(aruack)
trainer.train("chatterbot.corpus.english")

# Initialize the speech recognizer
r = sr.Recognizer()

# Define a function to get user input through voice
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            print("Sorry could not recognize what you said")
            return listen()

# Define a function to get user input through typing
def get_input():
    request = input('You: ')
    return request

# Definea function to generate a response from the chat bot
def respond(request):
    response = aruack.get_response(request)
    return str(response)

# Define a command-line interface for Aruack
class AruackInterface(cmd.Cmd):
    prompt = 'Aruack> '

    def do_listen(self, line):
        """Get user input through voice"""
        request = listen()
        response = respond(request)
        print(response)

    def do_talk(self, line):
        """Get user input through typing"""
        request = get_input()
        response = respond(request)
        print(response)

    def do_quit(self, line):
        """Quit the interface"""
        return True

# Start the command-line interface
interface = AruackInterface()
interface.cmdloop()
