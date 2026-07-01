def chatbot():
    print("=" * 45)
    print("        WELCOME TO BASIC CHATBOT")
    print("=" * 45)
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.🤝😊")
        elif user == "hi":
            print("Bot: Hello!👋")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "what is your name?":
            print("Bot: My name is Basic Chatbot.")
        elif user == "who created you":
            print("Bot: I was created using Python🐍.")
        elif user == "thank you":
            print("Bot: You're welcome!😍")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day💙.")
            break
        else:
            print("Bot: Sorry, I don't understand that😵.")

chatbot()
