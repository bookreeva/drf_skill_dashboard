from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """ Класс тестирования модели пользователя. """

    def setUp(self) -> None:
        """ Подготовка тестового окружения для тестирования. """

        self.user = User.objects.create(
            email='lola@join.com',
            password='123qwe456rty'
        )

        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """ Тестирование регистрации нового пользователя. """

        data = {
            'email': 'testuser@test.com',
            'password': 'testpassword',
            'telegram_id': '1234567890'
        }

        response = self.client.post(
            '/users/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_view_user_list(self):
        """ Тестирование просмотра списка пользователей. """

        # Просматривать список может только суперпользователь.
        response = self.client.get(
            '/users/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertEqual(
            response.json(),
            {
                'detail': 'У вас недостаточно прав для выполнения данного действия.'
            }
        )

    def test_view_user_detail(self):
        """ Тестирование просмотра профиля пользователя. """

        response = self.client.get(
            f'/users/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_user(self):
        """ Тестирование редактирования профиля пользователя. """

        data = {
            'email': 'lola@join.com',
            'telegram_id': '1234123421'
        }

        response = self.client.put(
            f'/users/{self.user.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_user(self):
        """ Тестирование удаления профиля пользователя. """

        response = self.client.delete(
            f'/users/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
