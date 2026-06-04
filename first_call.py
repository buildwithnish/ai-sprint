import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load your API key from the .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
model = genai.GenerativeModel("gemini-2.5-flash")

# Send your first message
response = model.generate_content(
    "What is a large language model? Explain in 3 sentences."
)

# Print the reply
print(response.text)
print(f"\nInput tokens:  {response.usage_metadata.prompt_token_count}")
print(f"Output tokens: {response.usage_metadata.candidates_token_count}")
print(f"Total tokens:  {response.usage_metadata.total_token_count}")
