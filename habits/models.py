from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

from habits.services import Place, Frequency
from users.models import NULLABLE


class Habit(models.Model):
    """ Модель привычки. """
    action = models.CharField(max_length=70,
                              default='Пить воду',
                              verbose_name='Привычка')
    place = models.CharField(choices=Place.choices,
                             default=Place.HOME,
                             verbose_name='Место выполнения привычки')
    on_time = models.DateTimeField(verbose_name='Время начала выполнения привычки',
                                   **NULLABLE)
    lead_time = models.PositiveIntegerField(validators=[MaxValueValidator(120)],
                                            verbose_name='Время на выполнение',
                                            help_text='Не более 120 секунд',
                                            **NULLABLE)
    frequency = models.CharField(choices=Frequency.choices,
                                 default=Frequency.DAILY,
                                 verbose_name='Периодичность')

    # (is_habit, enjoyable_habit) и reward - взаимоисключаемые поля.
    is_habit = models.BooleanField(default=False,
                                   verbose_name='Использовать приятную привычку',
                                   **NULLABLE)
    healthy_habit = models.ForeignKey('Habit',
                                      on_delete=models.SET_NULL,
                                      verbose_name='Привычка',
                                      help_text='Вы можете использовать одно из двух: '
                                                'указать полезную привычку или вознаграждение.',
                                      **NULLABLE)
    reward = models.CharField(max_length=150,
                              verbose_name='Вознаграждение за выполнение',
                              help_text='Вы можете использовать одно из двух: '
                                        'указать полезную привычку или вознаграждение.',
                              **NULLABLE)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name='Создатель привычки',
                                default=1,
                                **NULLABLE)
    is_published = models.BooleanField(default=False,
                                       verbose_name='Признак публичности')

    def clean(self):
        """
        Проверяет взаимоисключение полей
        reward, enjoyable_habit, healthy_habit.
        """
        if self.reward and self.healthy_habit:
            raise ValidationError('Поля вознаграждения, полезной и приятной '
                                  'привычки не могут быть заполнены одновременно.')

    def save(self, *args, **kwargs):
        """ Сохраняет объект после выполнения проверок в методе clean(). """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """ Возвращает строковое представление о модели привычки. """
        return f'{self.action}'

    class Meta:
        """ Метаданные для модели привычки. """
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
