#!/usr/bin/env python3
# coding: utf-8
from wxpy import *
import time

SourceSavePath = '.\\ReceiveFile\\'

bot = Bot()
tuling = Tuling(api_key='')

@bot.register()
def auto_reply_all(msg):

    print(msg)
    if isinstance(msg.chat, Group) and not msg.is_at:
      return
    elif msg.type == 'Text':
      time.sleep(2)
      tuling.do_reply(msg)
    elif msg.type == 'Picture':
      savePath = SourceSavePath+msg.file_name
      msg.get_file(savePath)
      msg.reply_image(savePath)
    else:
      msg.forward(msg.sender)
bot.join()
