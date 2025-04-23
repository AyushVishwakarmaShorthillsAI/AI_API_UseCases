import cohere
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("COHERE_API_KEY")

# messages for remembering the past conversations ;->
messages_Arr=[]

# function for chatting 
def chatFn():
    global messages_Arr  # 👈 this line makes sure you're using the outer variable
    prompt = input("Enter the prompt: ")
    
    req = {'role': 'user', 'content': prompt}
    messages_Arr.append(req)

    co = cohere.ClientV2(api_key)

    response = co.chat(
        model="command-a-03-2025",
        messages=messages_Arr
    )

    res_ans = response.message.content[0].text
    res = {"role": "assistant", "content": res_ans}
    messages_Arr.append(res)

    print("The fetched response:")
    print(res_ans)

exit='N'
while(exit!='Y' or exit!='y'):
    chatFn()
    print()
    exit=input('If you want to exit/quit asking questions ?, press y or Y for exiting, otherwise press any other key : ')
    if(exit=='Y' or exit=='y'):
        break

# print(messages_Arr)