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
prompt1 ="Hi!"
prompt2 ="explain time travel in 100 words"
prompt3="write a 100 word essay on machine learning"

prompts = [prompt1, prompt2, prompt3]  # Create a list of prompts to send to the model

# looping over the prompts and sending each one to the model for completion.
for prompt in prompts:   
    message ={
    "role":role,
    "content":prompt
}
    messages = [message] 
    response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=5000
    )
    usage=response.usage
    print(f"Prompt: {prompt} -->Your tokens:{usage.prompt_tokens} completions tokens:{usage.completion_tokens} total tokens:{usage.total_tokens} Finish reason:{response.choices[0].finish_reason}")
    
# message ={
#     "role":role,
#     "content":prompt
# }
# messages = [message]  # Create a list of messages to send to the model

# response = client.chat.completions.create(
#     model=model,
#     messages=messages,)
# print(response)

# print("#############################################")
# answers= response.choices[0].message.content  # Extract the content of the response message
# print(answers)  