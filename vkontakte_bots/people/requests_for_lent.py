import vk_api
import datetime


LOGIN = LOGIN
PASSWORD = PASSWORD

def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login=login, password=password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    
    vk = vk_session.get_api()
    response = vk.wall.get(count=5)
    if response['items']:
        for i in response['items']:
            print(f'{i["text"]};')
            date = datetime.datetime.fromtimestamp(i['date'])
            print(f"date: {date.strftime('%Y-%m-%d')}, time: {date.strftime('%H:%M:%S')}")
            

if __name__ == '__main__':
    main()
