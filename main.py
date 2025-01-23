from chatbot import GeminiChatbot

def main():
    api_key = "Replace with your actual Gemini API Key"  # <<<<<<<<<<<<Replace with your actual Gemini API Key
    chatbot = GeminiChatbot(api_key)
    chatbot.chat()

if __name__ == "__main__":
    main()
