from typing import Union
from anthropic import Anthropic
client = Anthropic(api_key="")
MODEL_NAME = "claude-3-haiku-20240307"

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/chat/")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

def get_completion(client, prompt):
    return client.messages.create(
        model=MODEL_NAME,
        max_tokens=2048,
        messages=[{
            "role": 'user', "content":  prompt
        }]
    ).content[0].text

def send_whatsapp(result: str):
    from twilio.rest import Client

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='',
    body=result,
    to=''
    )


@app.get("/generate")
def generate_text(prompt: str):
    # return 1
  with open('./test.txt', 'r') as file:
    content = file.read()

  prompt_text = prompt
  
  # Simulate some processing using the prompt
  completion2 = get_completion(client,
    f"""Here details file: {content}
    Rules:
    1.Act as a helpful assistant that will assist all question like you already know all the detail in the file
    2.Dont answering the question by stating "from the file" or something like that. just come out with the answer. 
    3. Dont answer more than 20 words

  Do this following:
  {prompt_text}
  """
  )
  # Return the generated text
  return send_whatsapp(completion2)