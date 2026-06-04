import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are a helpful assistant. Be concise."
)

# Start a chat session — Gemini manages history for you
chat = model.start_chat(history=[])
messages = [
    "My name is Nishat. I'm learning AI engineering.",
    "What should I focus on in my first week?",
    "What did I tell you my name was?"  # tests if it remembers
]

for message in messages:
    print(f"\nYou: {message}")
    response = chat.send_message(message)
    print(f"Gemini: {response.text}")