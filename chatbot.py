import requests
import json
from colorama import Fore, Style
import time
import sys

class GeminiChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"

    def simulate_typing(self, text, delay=0.009):

        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def send_message(self, message):
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": message}
                    ]
                }
            ]
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(self.url, headers=headers, json=data)

        if response.status_code == 200:
            try:
                result = response.json()
                ai_reply = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response from AI.")
                return ai_reply
            except json.JSONDecodeError:
                return "Error parsing the response."
        else:
            return f"Error {response.status_code}: {response.text}"

    def color_code_response(self, response):

        response = response.replace('`', "")  # Remove code
        colored_response = ""

        #blue
        for char in response:
            if char.isdigit():
                colored_response += Fore.BLUE + char + Style.RESET_ALL
            #  green
            elif char == ' ' and len(colored_response) > 0 and colored_response[-1] == '`':
                colored_response += Fore.GREEN + char + Style.RESET_ALL
            elif char == '`':
                colored_response += Fore.GREEN + char + Style.RESET_ALL
            #  bold
            elif char == '*':
                if len(colored_response) > 0 and colored_response[-1] != '\033[1m':
                    colored_response += '\033[1m'  # Start bold
                elif colored_response[-1] == '\033[1m':
                    colored_response += '\033[0m'  # End bold
            else:
                colored_response += char

        return colored_response

    def display_welcome_message(self):
        welcome_message = Fore.GREEN + "Chatbot: Hello there! How can I assist you today?" + Style.RESET_ALL
        self.simulate_typing(welcome_message)

    def display_exit_message(self):
        exit_message = Fore.RED + "Chatbot: Goodbye! It was a pleasure assisting you. See you soon!" + Style.RESET_ALL
        self.simulate_typing(exit_message)

    def chat(self):
        self.display_welcome_message()
        while True:
            user_input = input(Fore.YELLOW + "You: " + Style.RESET_ALL)

            if user_input.lower() in ['exit', 'quit', 'bye']:
                self.display_exit_message()
                break

            response = self.send_message(user_input)
            colored_response = self.color_code_response(response)

            # Output
            self.simulate_typing(Fore.CYAN + f"Chatbot: {colored_response}" + Style.RESET_ALL)
