# Step 1: Function to get a reply from the bot
def get_reply(user_input):
    user_input = user_input.lower()
    if user_input == "hello":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "My name is RuleBot!"

    elif user_input == "tell me a joke":
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    elif user_input == "thanks":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! See you later!"

    else:
        return "Sorry, I don't understand. Try: hello, how are you, bye"

# Step 2: Main loop to keep the chat going
print("Bot is ready! Type 'bye' to stop.")
print("------------------------------------")

while True:

    # Step 3: Take input from the user
    user_input = input("You: ")

    # Step 4: Get the bot's reply
    reply = get_reply(user_input)

    # Step 5: Print the reply
    print("Bot:", reply)

    # Step 6: Stop the loop if user says bye
    if user_input.lower() == "bye":
        break
