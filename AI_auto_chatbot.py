import os
from google import genai #pip install genai
from google.genai import types

# API KEY
#make you API key in google ai studio
api_key = ("enter here you api_key")

if not api_key:
    print("API KEY did not found!")
    exit()

# AI CLIENT
client = genai.Client(api_key=api_key)

# CHAT SESSION
chat = client.chats.create(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction="""
        You are MINI AI, a helpful AI assistant.
        You can speak Hindi, Hinglish and English.
        Give clear and beginner-friendly answers.
        """
    )
)

print("\n================================")
print("       MINI AI CHATBOT")
print("================================")
print("AI Status: Online")
print("Type 'exit' to close chatbot.")
print("--------------------------------")

# MAIN LOOP
while True:

    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("\nMINI AI: Goodbye!")
        break

    if not user_input:
        continue

    try:
        response = chat.send_message(user_input)

        print("\nMINI AI:", response.text)

    except Exception as e:
        print("\nError:", e)

client.close()


    
