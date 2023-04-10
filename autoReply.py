#!/usr/bin/env python3
# coding: utf-8
from wxpy import *
import time

SourceSavePath = '.\\ReceiveFile\\'

bot = Bot()

# 调用机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    apikey="xxx"
    headers = {'Authorization': apikey,}
    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': text}]
    }
    r = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)
    rjson=r.json()
    retext = "chatGPT:" + rjson["choices"][0]["text"]
    print(retext)
    return retext

@bot.register()
def auto_reply_all(msg):
    print(msg)
    if isinstance(msg.chat, Group) and not msg.is_at:
      return
    elif msg.type == 'Text':
      return auto_reply(msgs)
    else:
      msg.forward(msg.sender)
bot.join()
