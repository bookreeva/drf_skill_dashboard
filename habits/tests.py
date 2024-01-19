from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from habits.models import Habit
from habits.tasks import send_daily_habit_messages
from users.models import User


class HabitTestCase(APITestCase):
    """ Класс тестирования модели привычки. """

    def setUp(self) -> None:
        """ Подготовка тестового окружения для тестирования. """

        self.user = User.objects.create(
            email='lola@join.com',
            password='123qwe456rty',
            telegram_id='1756385524'
        )

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            action='позвонить родителям',
            is_published=True,
            frequency='ONE',
            reward='съесть печеньку',
            on_time=timezone.now(),
            creator=self.user
        )

    def test_create_habit(self):
        """ Тестирование создания привычки. """

        data = {
            'action': 'выбросить мусор',
        }

        response = self.client.post(
            reverse('habits:habit-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_view_habits_list(self):
        """ Тестирование просмотра списка опубликованных привычек. """

        response = self.client.get(
            reverse('habits:habit-list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_view_my_habits_list(self):
        """ Тестирование просмотра списка своих привычек. """

        response = self.client.get(
            reverse('habits:my-habits')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_view_habit_detail(self):
        """ Тестирование просмотра конкретной привычки. """

        response = self.client.get(
            reverse('habits:habits', args=[self.habit.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        """ Тестирование редактирования конкретной привычки. """

        data = {
            'reward': 'взять овсяную печеньку'
        }

        response = self.client.put(
            reverse('habits:habit-update', args=[self.habit.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habit(self):
        """ Тестирование удаления конкретной привычки. """

        response = self.client.delete(
            reverse('habits:habit-delete', args=[self.habit.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class MessageSendTestCase(APITestCase):
    """ Класс тестирования модели привычки. """

    def setUp(self) -> None:
        """ Подготовка тестового окружения для тестирования. """

        self.user = User.objects.create(
            email='lola@join.com',
            password='123qwe456rty',
            telegram_id='1756385524'
        )

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            action='позвонить родителям',
            is_published=True,
            frequency='ONE',
            reward='съесть печеньку',
            on_time=timezone.now(),
            creator=self.user
        )

    def test_send_daily_message(self):
        """ Тестирование таска отправки ежедневных привычек. """

        self.assertEqual(
            send_daily_habit_messages(),
            'OK'
        )
