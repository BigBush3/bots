import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

TOKEN = 'b067dde633a189641549efa6f0c6296b233949b53ac9505e1955dbf8bc1db58bed1ec8b10ab3c770d765e'

vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)


def send_message(chat_id, text):
    random_id = random.randint(0, 1000000)
    vk.method('messages.send' , {'chat_id': chat_id, 'message': text, 'random_id' : random_id})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                bad_words = ['привет', 'пока']
                msg = event.text
                chat_id = event.chat_id
                if msg in bad_words:
                    send_message(chat_id, 'вы использовали плохие слова')
                else:
                    send_message(chat_id, msg)