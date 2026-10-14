# Rule-Based ChatBot Buddy

import datetime
import time

name = input("Please enter your name: ")
presentHr = datetime.datetime.now().hour

if 5 <= presentHr <= 11:
    print("Good Morning,", name)
elif 11 <= presentHr <= 17:
    print("Good Afternoon,", name)
elif 17 <= presentHr <= 20:
    print("Good Evening,", name)
else:
    print("Good Night,", name)


print("Welcome! To Our ChatBot.")
print("Hey! I am Rule-Based Chatbot. You can ask me basic questions.")


# Chatbot memory creation [dictionary type]
responses = {
    "hello": "Oh! hi, welcome. How I can help you?",
    "give me your intro": "Yes Ofcourse! I am a Rule-Based Chatbot. I give you answer of those quesitons which is written in my program only.",
    "i am not happy": "Oh! what happened, why are you not felling happy?",
    "i am so happy": "Feels so great to hear that. I wish you stay always happy :)",
    "i am sad":"HUHH! what happened, why are you sad. Is everything okay?",
    "i am not sad": "Ohkay! Are you feels netural, or you want some interesting thing?",
    "how was your day": "I am so happy! because am talking with you :)",
    "i want a good friend who can talk with me": "Seriously, am here with you. You can talk with me. I can be your best friend."
}

# Method/Function to get response of chatbot
def getResponse(userQues):
    userQues = userQues.lower()
    for each in responses:
        if each in userQues:
            return responses[each]

    return "So Sorry! I am not able to answer this, because this is not in my memory."

# Take user input
while True:
    userInput = input("Enter your question: ")

    if "bye" in userInput.lower():
        print("Chatbot: Goodbye! It was nice talking with you.")
        break

    reply = getResponse(userInput)
    print("ChatBot: ", reply)