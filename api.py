import os
import openai

openai.api_key = os.environ['OPENAI_APT']

def get_gpt_response(prompt,max_tokens=1000):
  responce = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}],
    max_tokens=max_tokens
    )
  responce_message = responce.to_dict()['choices'][0]['message']['content']
  return responce_message



