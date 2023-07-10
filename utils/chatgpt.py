import openai
import time
import re
from utils.stablediffusion import generate


def send(historyMessages, msg):
    historyMessages.append({'role': 'user', 'content': msg})
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k-0613',
        messages=historyMessages,
        temperature=0,
        stream=True,  # again, we set stream=True,
        api_key=""
    )

    collected_messages = []
    for chunk in response:
        chunk_message = chunk['choices'][0]['delta']  # extract the message
        collected_messages.append(chunk_message)  # save the message
        print(chunk_message.get('content', ''), end="")
    print()
    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    return full_reply_content
