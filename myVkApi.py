import os
import random
from io import BytesIO
import requests

import vk_api
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard

tkn = os.getenv("TOKEN")
groupId = os.getenv("GROUP_ID")
vk = vk_api.VkApi(token=tkn)
longpoll = VkBotLongPoll(vk, groupId)
upload = VkUpload(vk)

def upload_photo(upload, url):
    img = requests.get(url).content
    f = BytesIO(img)

    response = upload.photo_messages(f)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def send_photo(vkPhoto, peer_id, message, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    vkPhoto.method("messages.send",
                   {"peer_id": peer_id, "message": message,
                    "attachment": attachment,
                    "random_id": 0})


def write_msg(peer_id, message, keyboard):
    vk.method('messages.send',
              {'peer_id': peer_id,
               'keyboard': keyboard,
               'message': message,
               'random_id': random.randint(0, 2048)})


def create_empty_keyboard():
    keyboard = vk_api.keyboard.VkKeyboard.get_empty_keyboard()

    return keyboard


def create_keyboard():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=False)

    keyboard.add_button("/Фотожаба", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

    keyboard.add_line()

    keyboard.add_button("/Ква-котик", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

    keyboard.add_line()

    keyboard.add_button("/Ква-мотивация", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

    return keyboard.get_keyboard()

