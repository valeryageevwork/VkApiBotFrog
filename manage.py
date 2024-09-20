import os
import time

from vk_bot import *
from myVkApi import *

try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            bot = VkBot()

            keyboard = create_keyboard()
            empty_keyboard = create_empty_keyboard()

            message = event.obj['message']
            lowMessageText = str.lower(message['text'])
            lowMessageText = str.replace(lowMessageText, '[club226963554|@frog_nyashnost_bot] ', '')

            if lowMessageText == '/помощь':
                write_msg(message['peer_id'], bot.new_message(lowMessageText), keyboard)
            elif lowMessageText == '/ква-котик':
                send_photo(vk, message['peer_id'], "Муррр.. муррквак.. :з",*upload_photo(upload, bot.new_message(lowMessageText)))
            elif lowMessageText == '/фотожаба':
                send_photo(vk, message['peer_id'], "Квак.. Квак-ква :)", *upload_photo(upload, bot.new_message(lowMessageText)))

            elif lowMessageText == '/ква-мотивация':
                write_msg(message['peer_id'], bot.new_message(lowMessageText), keyboard)

except Exception as e:
    print(e)
