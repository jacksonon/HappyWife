#!/usr/bin/env python3
# coding: utf-8
from wxpy import *
bot = Bot()
tuling = Tuling(api_key='你的key')
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        tuling.do_reply(msg)
bot.join()
