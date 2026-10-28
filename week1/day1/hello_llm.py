import os 
from pathlib import Path
from dotenv import load_dotenv  
from groq import Groq

load_dotenv()  # Load environment variables from .env file
my_api_key = os.getenv("GROQ_API_KEY")  # Retrieve the API key from environment variables
if not my_api_key:
    raise ValueError("API key kaha hai bhai?")  # Raise an error if the API key is not found

client = Groq(api_key=my_api_key)  # Initialize the Groq client with the API key

model = "openai/gpt-oss-120b"  # Specify the model mode to use
role="user"
prompt ="Do you know Padho with Pratyush"
message ={
    "role":role,
    "content":prompt
}
messages = [message]  # Create a list of messages to send to the model

response = client.chat.completions.create(
    model=model,
    messages=messages,)
print(response)

print("#############################################")
answers= response.choices[0].message.content  # Extract the content of the response message
print(answers)  