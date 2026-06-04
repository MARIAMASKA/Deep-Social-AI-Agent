import os
from dotenv import load_dotenv
from google import genai

print("File started")

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("GOOGLE_API_KEY is missing. Check your .env file.")
    exit()

print("API key found")

client = genai.Client(api_key=api_key)

print("Available models for your Gemini API key:")
print("-" * 50)

for model in client.models.list():
    print(model.name)