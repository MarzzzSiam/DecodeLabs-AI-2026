"""
DecodeLabs AI Internship - Project 1
Rule-Based AI Chatbot
"""

# ---- Knowledge Base ----
responses = {
    'hello': 'Hi there! How can I help you today?',
    'hi': 'Hello! Nice to see you.',
    'how are you?': "I'm just a bunch of code, but I'm doing great!",
    'what is your name?': 'I am Marzon, your friendly rule-based assistant.',
    'who made you?': 'I was built by Marzan as part of the DecodeLabs AI Internship.',
    'tell me a joke': "Why do programmers prefer dark mode? Because light attracts bugs.",
    'help': 'I can chat about greetings, my name and how I am doing. Try "hello" or "help"!',
    'thanks': "You're welcome!",
    'thank you': "You're welcome!",
}

# Fallback message
DEFAULT_RESPONSE = "I do not understand. Type 'help' to see what I can do or 'exit' to quit."

# Words that will end the conversation
EXIT_COMMANDS = {'exit', 'bye', 'quit', 'goodbye'}


def get_response(user_input: str) -> str:
    """Look up a cleaned user input in the knowledge base, with fallback."""
    return responses.get(user_input, DEFAULT_RESPONSE)


def run_chatbot():
    print("Marzon: Hello! I'm your rule-based chatbot. Type 'exit' to quit.\n")

    while True:
        raw_input_text = input("You: ")
        clean_input = raw_input_text.lower().strip()

        # Exit condition
        if clean_input in EXIT_COMMANDS:
            print("Marzon: Goodbye! Have a great day.")
            break

        # Process and respond
        reply = get_response(clean_input)
        print(f"Marzon: {reply}")


if __name__ == "__main__":
    run_chatbot()
