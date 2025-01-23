import json

def save_conversation(conversation_history, filename="conversation_history.json"):

    with open(filename, "w") as file:
        json.dump(conversation_history, file, indent=4)
    print("Conversation history saved.")

def load_conversation(filename="conversation_history.json"):

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
