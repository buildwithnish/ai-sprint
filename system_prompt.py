import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

question="What is Machine Learning?"

#version 1: no system prompt
model_plain=genai.GenerativeModel("gemini-2.5-flash")
response_plain=model_plain.generate_content(question)
print("No system prompt:")
print(response_plain.text)

#version 2: with system prompt
model_cricket=genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""You are an expeert cricket analyst from Chennai. 
    You explain technical concepts using cricket analogies.
    Keep all answers under 4 sentences.
    Always end with a cricket example.""")
response_cricket=model_cricket.generate_content(question)
print("\nWith system prompt:")
print(response_cricket.text)

#version 3: with a strict professional prompt
model_pro = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""You are a senior software engineer at Google.
Give technically precise answers.
No analogies. Use proper terminology.
Maximum 3 sentences."""
)
response_pro = model_pro.generate_content(question)
print("\n=== With professional system prompt ===")
print(response_pro.text)