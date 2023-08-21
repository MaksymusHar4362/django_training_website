import requests
from .models import TeleSettings

def sendTelegram(tg_n, tg_p):
    settings = TeleSettings.objects.get(pk=1)

    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)

    api = "https://api.telegram.org/bot"
    method = api + token + '/sendMessage'

    part_1 = text[0:text.find('{')]
    part_2 = text[text.find('}')+1:text.rfind('{')]
    part_3 = text[text.rfind('}'):-1]

    text_s = part_1 + tg_n + part_2 + tg_p + part_3

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_s
        })
