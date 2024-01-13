import requests
from django.db import models
from django.conf import settings


class Place(models.TextChoices):
    """ Класс choices для поля 'place'. """
    HOME = 'дома', 'дома'
    KITCHEN = 'на кухне', 'на кухне'
    PARKING = 'на парковке', 'на парковке'
    POOL = 'в бассейне', 'в бассейне'
    LIBRARY = 'в библиотеке', 'в библиотеке'
    COFFEE_SHOP = 'в кофейне', 'в кофейне'
    GARDEN = 'в саду', 'в саду'
    PARK = 'в парке', 'в парке'
    OFFICE = 'на работе', 'на работе'
    WALK = 'на прогулке', 'на прогулке'
    FITNESS_ROOM = 'в тренировочном зале', 'в тренировочном зале'
    SHOP = 'в магазине', 'в магазине'


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
