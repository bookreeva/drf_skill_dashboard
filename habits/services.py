import requests
from django.db import models
from django.conf import settings


class Place(models.TextChoices):
    """ Класс choices для поля 'place'. """
    HOME = 'HOME', 'дома'
    KITCHEN = 'KCHEN', 'на кухне'
    PARKING = 'PING', 'на парковке'
    POOL = 'POOL', 'в бассейне'
    LIBRARY = 'LARY', 'в библиотеке'
    COFFEE_SHOP = 'CHOP', 'в кофейне'
    GARDEN = 'GDEN', 'в саду'
    PARK = 'PARK', 'в парке'
    OFFICE = 'OICE', 'на работе'
    WALK = 'WALK', 'на прогулке'
    FITNESS_ROOM = 'FOOM', 'в тренировочном зале'
    SHOP = 'SHOP', 'в магазине'


class Frequency(models.TextChoices):
    """ Класс choices для поля 'frequency'. """
    DAILY = 'ONE', 'ежедневно'
    WEEKLY = 'WEEK', 'один раз в неделю'


def send_tg_message(telegram_id, text):
    """ Отправляет сообщение в телеграм по 'chat_id'. """
    url = settings.TELEGRAM_API_URL
    token = settings.TELEGRAM_API_TOKEN

    try:
        requests.post(
            url=f'{url}{token}/sendMessage',
            data={
                'chat_id': telegram_id,
                'text': text
            }
        )
    except Exception as e:
        return f'Ошибка отправки: {str(e)}'
    else:
        return f'Сообщение отправлено'
