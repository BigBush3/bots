import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random



TOKEN = 'b067dde633a189641549efa6f0c6296b233949b53ac9505e1955dbf8bc1db58bed1ec8b10ab3c770d765e'

def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 203772710)

    for event in longpoll.listen():
        print(event.type)
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Спасибо, что написали нам. Мы обязательно ответим",
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()