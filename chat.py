# Simple Chatbot in Python
# this python program can be used to generate a simple chatbot, incase u need to improvise,you can also use list, dictionaries for a better
#comment "help for any changes"
def chatbot():
    print("Hello! I am your friendly chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input.lower():
            print("Chatbot: Hi there! How can I assist you today?")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm just a bunch of code, but I'm functioning perfectly. Thanks for asking!")
        elif "name" in user_input.lower():
            print("Chatbot: I'm just a humble chatbot without a fancy name. But you can call me Bot!")
        else:
            print("Chatbot: I'm still learning. Could you try asking something else?")

# Start the chatbot
if __name__ == "__main__":
    chatbot()
