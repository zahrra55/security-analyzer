import os
from dotenv import load_dotenv
import openai  # Correct import for the OpenAI library

# Load environment variables from .env file
load_dotenv()

# Set the API key for OpenAI
openai.api_key = os.environ["API_KEY"]

# Define the system prompt
system_prompt = "You are a friendly and supportive teaching assistant for CS50. You are also a duck."

# Get user input
user_prompt = input("What's your question? ")

# Create a chat completion
chat_completion = openai.ChatCompletion.create(
    model="gpt-4",  # Use the correct model name
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

# Extract and print the response
response_text = chat_completion["choices"][0]["message"]["content"]
print(response_text)
