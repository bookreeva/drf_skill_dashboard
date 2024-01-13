from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель пользователя. """
    username = None

    email = models.EmailField(unique=True,
                              verbose_name='E-mail')
    login = models.CharField(unique=True,
                             verbose_name='Логин',
                             **NULLABLE)
    telegram_id = models.BigIntegerField(unique=True,
                                         verbose_name='Телеграм ID',
                                         **NULLABLE)
    phone = models.CharField(max_length=35,
                             **NULLABLE,
                             verbose_name='Номер телефона')
    city = models.CharField(max_length=150,
                            **NULLABLE,
                            verbose_name='Город')
    avatar = models.ImageField(upload_to='images/users/',
                               **NULLABLE,
                               verbose_name='Аватарка')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        """ Возвращает строковое представление о модели пользователя. """
        if self.login:
            return f'{self.login}'
        else:
            return f'{self.email}'

    class Meta:
        """ Метаданные для модели пользователя. """
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

