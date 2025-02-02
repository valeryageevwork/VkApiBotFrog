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
            lowMessageText = str.replace(lowMessageText, '[club229149546|@smart_kotyambus] ', '')

            if lowMessageText == '/старт':
                write_msg(message['peer_id'], 'Мурр... Старт!', keyboard)

            elif lowMessageText == '/обновление':
                write_msg(message['peer_id'], 'Котик перезагружается..', keyboard)

            elif lowMessageText == '/котик':
                send_attachment(vk, message['peer_id'], "Муррр.. :)",
                                *upload_attachment(upload, bot.new_message(lowMessageText)))
            elif lowMessageText == '/собачка':
                send_attachment(vk, message['peer_id'], "Мургавc..! :з",
                                *upload_attachment(upload, bot.new_message(lowMessageText)))
            elif lowMessageText == "/муркосмос":
                send_attachment(vk, message['peer_id'], "Земля в иллюминаторе.. Мурлечный путь..",
                                *upload_attachment(upload, bot.new_message(lowMessageText)))
            elif lowMessageText == '/мотивация':
                write_msg(message['peer_id'], bot.new_message(lowMessageText), keyboard)

except Exception as e:
    print(e)
