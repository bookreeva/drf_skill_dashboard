from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_daily_habit_messages():
    """ Отправляет сообщение в телеграм о привычке. """
    current_time = timezone.now()

    time_start_task = timezone.now() - timedelta(minutes=1)

    habits = Habit.objects.filter(on_time__gte=time_start_task, frequency='ONE')

    try:
        for habit in habits.filter(on_time__lte=current_time):
            user = habit.creator
            telegram_id = user.telegram_id

            text = f"""Напоминание о выполнении привычки: 
{habit.action.title()}.
Место: {habit.place}.
У вас есть: {habit.lead_time} секунд 💪"""

            if habit.reward:
                result = text + f'\nВознаграждение: {habit.reward}.'
            elif habit.healthy_habit:
                result = text + f'\nДополните вашей приятной привычкой: {habit.healthy_habit}.'

            send_tg_message(telegram_id, result)
    except Exception as e:
        return f'Ошибка таска: {str(e)}.'
    else:
        return 'OK'


@shared_task
def send_weekly_habit_messages():
    """ Отправляет сообщение в телеграм о привычке. """
    current_weekday = timezone.now().weekday()
    current_time = timezone.now()
    time_start_task = timezone.now() - timedelta(minutes=1)

    habits = Habit.objects.filter(on_time__gte=time_start_task, frequency='WEEK')

    try:
        for habit in habits.filter(on_time__lte=current_time):
            if habit.on_time.weekday() == current_weekday:
                user = habit.creator
                telegram_id = user.telegram_id

                text = f"""Напоминание о выполнении привычки: 
{habit.action}.
Место: {habit.place}.
У вас есть: {habit.lead_time} секунд 💪"""

                if habit.reward:
                    result = text + f'\nВознаграждение: {habit.reward}.'
                elif habit.healthy_habit:
                    result = text + f'\nДополните вашей приятной привычкой: {habit.healthy_habit}.'

                send_tg_message(telegram_id, result)
    except Exception as e:
        return f'Ошибка таска: {str(e)}.'
    else:
        return 'OK'

