import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "Write a one-sentence tagline for an AI startup."

# Loop through 3 temperatures
for temp in [0.1, 0.7, 1.5]:
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        generation_config={"temperature": temp}
    )
    response = model.generate_content(prompt)
    print(f"\n--- Temperature {temp} ---")
    print(response.text)