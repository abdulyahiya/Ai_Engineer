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
prompt ="Suggest a name for my clothing company"

# system_role
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggestame for my  company. name should be in one word, suggest one name only"
}

message ={
    "role":role,
    "content":prompt
}
messages = [message_system, message]  # Create a list of messages to send to the model

# temperature by default is 0.0, tange is 0 to 2

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2,)
# print(response)

print("#############################################")
answers= response.choices[0].message.content  # Extract the content of the response message
print(answers)  